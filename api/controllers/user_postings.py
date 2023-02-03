from flask import Blueprint, jsonify, request, make_response
from bson.objectid import ObjectId
from api.validators.application import validate_application
from api import mongo, app, andrewMongo

user_postings = Blueprint("user_postings", __name__) #sets up blueprint
# users = andrewMongo['why-phi-testing'].users #mongodb user collection 
users = mongo.db.user

def _return_exception(e):
    response_object = {
        "status": False,
        "message": str(e)
    }
    return jsonify(response_object)

#Fetches all user datas
@user_postings.route('/user/data/', methods=['GET'])
def get_all_users():

    all_users = []

    try:
        for posting in users.find():
            all_users.append(posting)

        response_object = {
            "status": True,
            "all_users": all_users,
            "message": 'All users received.'
        }
        return make_response(jsonify(response_object), 200)

    except Exception as e:
        return make_response(_return_exception(e), 400)

#Initializes a user with postings with empty dictionaries
@user_postings.route('/user/data/create/<user_id>', methods=['POST'])
def create_user_data(user_id):

    data = { "userKey": user_id }

    try:
        users.insert_one(data)

        response_object = {
            "status": True,
            "message": 'New user created successfully.'
        }
        return make_response(jsonify(response_object), 200)

    except Exception as e:
        return make_response(_return_exception(e), 400)

#get one user's all data
@user_postings.route('/user/data/all/<user_id>/<posting_id>', methods=['GET'])
def get_user_data_all(user_id, posting_id):

    user_posting_data = {}

    try:
        user_data = users.find_one({ "userKey": user_id })
        
        if not user_data: 
            users.insert_one({ "userKey": user_id })
            user_data = {}

        elif posting_id in user_data:
            user_posting_data = user_data[posting_id]

        response_object = {
            "status": True,
            "user_posting_data": user_posting_data,
            "message": 'User Posting Data Retrieved.'
        }
        return make_response(jsonify(response_object), 200)

    except Exception as e:
        return make_response(_return_exception(e), 400)

#get one user's data for a certain data type
@user_postings.route('/user/data/<data_type>/<user_id>/<posting_id>', methods=['GET'])
def get_user_data_one(data_type, user_id, posting_id):

    user_posting_data = {}

    try:
        user_data = users.find_one({ "userKey": user_id })
        print(user_data)
        if not user_data: 
            users.insert_one({ "userKey": user_id })
            user_data = {}

        elif posting_id in user_data:
            user_posting_data = user_data[posting_id][data_type]

        response_object = {
            "status": True,
            "user_posting_data": user_posting_data,
            "message": 'User Posting Data Retrieved.'
        }
        return make_response(jsonify(response_object), 200)

    except Exception as e:
        return make_response(_return_exception(e), 400)

#Updates each user -> posting -> read_list
@user_postings.route('/user/data/<data_type>/<user_id>/<posting_id>', methods=['POST'])
def update_user_data(data_type, user_id, posting_id):
    # return make_response(jsonify({"user": user_id, "post": posting_id}))
    
    data = request.get_json()

    try:
        users.update_one(
            {"userKey": user_id},
            {"$set": { posting_id+"."+data_type: data }}, 
        )
        response_object = {
            "status": True,
            "message": 'User data updated.'
        }
        return make_response(jsonify(response_object), 200)

    except Exception as e:
        print("error pushing to mongodb")
        return make_response(_return_exception(e), 402)

#delete a user's data
@user_postings.route('/user/data/delete/<user_id>', methods=['DELETE'])
def delete_user_data(user_id):

    try:
        users.delete_one({ "userKey": user_id })

        response_object = {
            "status": True,
            "message": 'User deleted.'
        }
        return make_response(jsonify(response_object), 200)

    except Exception as e:
        return make_response(_return_exception(e), 400)
        