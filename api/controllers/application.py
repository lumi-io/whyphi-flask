from flask import Blueprint, jsonify, request, make_response
from bson.objectid import ObjectId
from api.validators.application import validate_application
from api import mongo, app
import boto3
from botocore.exceptions import ClientError, WaiterError
import json
from time import time, ctime

from api.middlewares.application import decode_and_upload_base64_file, get_file_extension, parse_graduation_date

application = Blueprint("application", __name__)  # initialize blueprint
applications = mongo.db.applications

# Parameters for S3 bucket
BUCKET = app.config["S3_BUCKET_NAME"]
REGION = app.config["S3_REGION"]
s3_client = boto3.client("s3")


def _return_exception(e):
    response_object = {
        "status": False,
        "message": str(e)
    }
    return jsonify(response_object)


@application.route('/user/applications/<bucket_name>', methods=['POST'])
def delete_all(bucket_name):
    try:
        s3_client = boto3.client('s3')
        files = s3_client.list_objects(Bucket=bucket_name)['Contents']
        for file in files:
            s3_client.delete_objects(Bucket=bucket_name, Key=file["Key"])

    except Exception as e:
        return make_response(_return_exception(e), 400)


@application.route('/user/portal/submit/<posting_id>', methods=['POST'])
def submit_application(posting_id):
    """ Endpoint to append an application to a job posting """

    data = request.get_json()
    data["applicantId"] = ObjectId()
    data['timeApplied'] = ctime(time())
    data["gradYear"] = parse_graduation_date(data["gradYear"])

    resume_upload_path = posting_id + '/resume/' + \
        str(data["applicantId"]) + '_resume'
    image_upload_path = posting_id + '/image/' + \
        str(data["applicantId"]) + '_image'

    try:
        resume_url = decode_and_upload_base64_file(
            data["resume"], resume_upload_path)
        image_url = decode_and_upload_base64_file(
            data["image"], image_upload_path)

    except botocore.exceptions.ClientError as error:
        logging.warning(error)
        response_object = {
            "status": False,
            "message": 'Issues with AWS S3. Please contact administrator.'
        }
        return make_response(_return_exception(e), 400)
        
    except Exception as e:
        logging.warning(e)
        response_object = {
            "status": False,
            "message": e
        }
        return make_response(_return_exception(e), 400)

    data["resume"] = resume_url
    data["image"] = image_url

    try:
        applications.update(
            {"postingKey": ObjectId(posting_id)},
            {"$push": {"applications": data}}
        )
        response_object = {
            "status": True,
            "message": 'Application submitted.'
        }
        return make_response(jsonify(response_object), 200)

    except Exception as e:
        return make_response(_return_exception(e), 400)
