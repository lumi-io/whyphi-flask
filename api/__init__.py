import os
import json
import datetime
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode
from pymongo import MongoClient


class JSONEncoder(json.JSONEncoder):
    """ extend json-encoder class """

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, set):
            return list(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


# Objects and Instances to be used in other files are placed here
mongo = PyMongo()
app = Flask(__name__)
andrewMongo = MongoClient() #andrew's mongodb setup
CORS(app, supports_credentials=True)
oauth = OAuth(app)
auth0 = None


def create_app(test_config=False):
    """ Initializes and adds necessary information into the Flask app object """

    app.json_encoder = JSONEncoder

     # Setting up configurtion based on environment
    if test_config:
        app.config.from_pyfile('test_config.py')
    else:
        if app.config["ENV"] == "development":
            app.config.from_pyfile('config.py')
        elif app.config["ENV"] == "production":
            app.config.from_pyfile('prod_config.py')

    configure_mongo_uri(app, test_config)  # MongoDB configuration
    andrew_configure_mongo_uri(app, test_config)  # Andrew's MongoDB configuration
    register_blueprints(app)  # Registering blueprints to Flask App
    auth0 = oauth.register(
        'auth0',
        client_id=app.config["AUTH0_CLIENT_ID"],
        client_secret=app.config["AUTH0_SECRET"],
        api_base_url=app.config["AUTH0_API_BASE_URL"],
        access_token_url=app.config["AUTH0_ACCESS_TOKEN_URL"],
        authorize_url=app.config["AUTH0_AUTHORIZE_URL"],
        client_kwargs={
            'scope': 'openid profile email',
        },
    )

    # register error Handler
    # app.register_error_handler(Exception, all_exception_handler)

    return app


def configure_mongo_uri(app, test_config):
    """ Helper function to configure MongoDB URI """

    # Connecting Flask App with DB
    app.config["MONGO_URI"] = "mongodb+srv://"+app.config["MONGODB_USERNAME"] + \
        ":"+app.config["MONGODB_PASSWORD"]+"@"+app.config["MONGODB_HOST"]
    try:
        mongo.init_app(app)
        print("MongoDB connected.")
    except Exception as e:
        print(e)

def andrew_configure_mongo_uri(app, test_config):
    """ Helper function to configure MongoDB URI """
    andrewMongo = MongoClient(app.config['ANDREW_MONGODB_URI'])

    try:
        print("Andrew's MongoDB connected.")
    except Exception as e:
        print(e)

def register_blueprints(app):
    """ Helper function to register blueprints into Flask App """
    from api.controllers.admin_postings import job_post
    from api.controllers.application import application
    from api.controllers.admin_applications import admin_applications
    from api.controllers.general import general
    from api.controllers.auth import auth
    from api.controllers.user_postings import user_postings

    print("Registering Flask Blueprints.")
    app.register_blueprint(general)
    app.register_blueprint(job_post)
    app.register_blueprint(application)
    app.register_blueprint(admin_applications)
    app.register_blueprint(auth)
    app.register_blueprint(user_postings)

    # register error Handler
    # app.register_error_handler(Exception, all_exception_handler)

    return app
