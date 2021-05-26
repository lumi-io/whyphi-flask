# Flask Configuration file
import os
from dotenv import load_dotenv

load_dotenv()

FLASK_ENV = 'development'

MONGODB_DB = os.getenv('MONGODB_DB')
MONGODB_HOST = os.getenv('MONGODB_HOST')
MONGODB_PORT = int(os.getenv('MONGODB_PORT'))
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_DEV_NAME')

#s3 bucket access
S3_KEY = os.getenv("AWS_KEY")
S3_BUCKET= 'resume-testing-ats'
S3_SECRET= os.getenv("AWS_SECRET_ACCESS_KEY")

# class ProdConfig(Config):
#     FLASK_ENV = 'production'
#     DEBUG = False
#     TESTING = False
#     DATABASE_URI = environ.get('PROD_DATABASE_URI')


# class DevConfig(Config):
#     FLASK_ENV = 'development'
#     DEBUG = True
#     TESTING = True
#     DATABASE_URI = environ.get('DEV_DATABASE_URI')
