# Flask Test Configuration file
import os
from dotenv import load_dotenv

load_dotenv()

FLASK_ENV = 'test'

MONGODB_DB = os.getenv('MONGODB_TEST_DB')
MONGODB_HOST = os.getenv('MONGODB_TEST_HOST')
MONGODB_PORT = int(os.getenv('MONGODB_TEST_PORT'))
MONGODB_USERNAME = os.getenv('MONGODB_TEST_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_TEST_PASSWORD')

S3_BUCKET_NAME= os.getenv('S3_BUCKET_TEST_NAME')


#s3 bucket access
S3_KEY = os.getenv("AWS_KEY")
S3_BUCKET= 'resume-testing-ats'
S3_SECRET= os.getenv("AWS_SECRET_ACCESS_KEY")