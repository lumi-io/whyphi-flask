from flask import Blueprint, jsonify, request, make_response
from bson.objectid import ObjectId
from api.validators.application import validate_application
from api import mongo
import boto3
from botocore.exceptions import ClientError, WaiterError
import json
from time import time, ctime

application = Blueprint("application", __name__)  # initialize blueprint
applications = mongo.db.applications

# Parameters for S3 bucket
BUCKET = 'resume-testing-ats'
REGION = 'us-east-2'
s3_client = boto3.client('s3')


def return_exception(e):
    response_object = {
        "status": False,
        "message": str(e)
    }
    return jsonify(response_object)


@application.route('/user/portal/upload-resume/<posting_id>', methods=['POST'])
def upload_resume(posting_id, acl="public-read"):
    resume_data = request.files["file"]
    try:
        file = resume_data
        filename = file.filename
        response = s3_client.upload_fileobj(
            file,
            'resume-testing-ats',
            posting_id + '/resume/{}'.format(filename),
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
        return f"https://{BUCKET}.s3.{REGION}.amazonaws.com/" + posting_id + "/resume/{}".format(filename)
    except Exception as e:
        print(e)
        return make_response(return_exception(ClientError), 400)


@application.route('/user/portal/upload-image/<posting_id>', methods=['POST'])
def upload_image(posting_id, acl="public-read"):
    data = request.files["file"]
    try:
        file = data
        filename = file.filename
        response = s3_client.upload_fileobj(
            file,
            'resume-testing-ats',
            posting_id + '/profile-pic/{}'.format(filename),
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
        return f"https://{BUCKET}.s3.{REGION}.amazonaws.com/" + posting_id + "/profile-pic/{}".format(filename)
    except:
        return make_response(return_exception(ClientError), 400)

@application.route('/user/portal/upload-video/<posting_id>', methods=['POST'])
def upload_video(posting_id, acl="public-read"):
    data = request.files["file"]
    try:
        file = data
        filename = file.filename
        response = s3_client.upload_fileobj(
            file,
            'resume-testing-ats',
            posting_id + '/elevator-pitch/{}'.format(filename),
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
        return f"https://{BUCKET}.s3.{REGION}.amazonaws.com/" + posting_id + "/elevator-pitch/{}".format(filename)
    except:
        return make_response(return_exception(ClientError), 400)


# @application.route('/user/applications/upload', methods=['POST'])
def upload(resume_file, profile_pic_file, video_file, acl="public-read"):
    s3_client = boto3.client('s3')
    if resume_file:
        try:
            file = resume_file
            s3_client.upload_fileobj(
                file,
                'resume-testing-ats',
                'resume/{}'.format(file.filename),
                ExtraArgs={
                    "ACL": acl,
                    "ContentType": file.content_type
                })
        except Exception as e:
            return make_response(return_exception(e), 400)
    if profile_pic_file:
        try:
            file = profile_pic_file
            s3_client.upload_fileobj(
                file,
                'resume-testing-ats',
                'profile-pic/{}'.format(file.filename),
                ExtraArgs={
                    "ACL": acl,
                    "ContentType": file.content_type
                })
        except Exception as e:
            return make_response(return_exception(e), 400)
    if video_file:
        try:
            file = video_file
            s3_client.upload_fileobj(
                file,
                'resume-testing-ats',
                'elevator-pitch/{}'.format(file.filename),
                ExtraArgs={
                    "ACL": acl,
                    "ContentType": file.content_type
                })
            response_object = {
                "status": True,
                "message": 'files uploaded.'
            }
            return make_response(jsonify(response_object), 200)
        except Exception as e:
            return make_response(return_exception(e), 400)
    else:
        response_object = {
            "status": False,
            "message": 'Bad request parameters: {}'
        }
        return make_response(jsonify(response_object), 400)



@application.route('/user/applications/<bucket_name>', methods=['POST'])
def delete_all(bucket_name):
    try:
        s3_client = boto3.client('s3')
        files = s3_client.list_objects(Bucket=bucket_name)['Contents']
        for file in files:
            s3_client.delete_objects(Bucket=bucket_name, Key=file["Key"])

    except Exception as e:
        return make_response(return_exception(e), 400)


def update_filenames(posting_id, applicant_id, urls):
    applications.find_and_modify(
        query={
            "postingKey": ObjectId(posting_id),
            "applications.applicantId": ObjectId(applicant_id)
        },
        update={
            "resume": urls[0],
            "profilePic": urls[1],
            "elevatorPitch": urls[2]
        }
    )
    return True


@application.route('/user/portal/submit/<posting_id>', methods=['POST'])
def submit_application(posting_id):
    """ Endpoint to append an application to a job posting """

    data = request.get_json()
    data["applicantId"] = ObjectId()
    data['timeApplied'] = ctime(time())
    print(data)

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
        return make_response(return_exception(e), 400)
