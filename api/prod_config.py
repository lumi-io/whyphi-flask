# Flask Test Configuration file
import os
from dotenv import load_dotenv

load_dotenv()

FLASK_ENV = 'production'

MONGODB_DB = os.getenv('MONGODB_PROD_DB')
MONGODB_HOST = os.getenv('MONGODB_PROD_HOST')
MONGODB_PORT = int(os.getenv('MONGODB_PROD_PORT'))
MONGODB_USERNAME = os.getenv('MONGODB_PROD_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PROD_PASSWORD')

S3_BUCKET_NAME = os.getenv('S3_BUCKET_PROD_NAME')
S3_REGION = os.getenv('S3_REGION')


#s3 bucket access
S3_KEY = os.getenv("AWS_KEY")
S3_BUCKET= 'resume-testing-ats'
S3_SECRET= os.getenv("AWS_SECRET_ACCESS_KEY")

AUTH0_CLIENT_ID = os.getenv('AUTH0_CLIENT_ID')
AUTH0_SECRET = os.getenv('AUTH0_SECRET')
AUTH0_API_BASE_URL = os.getenv('AUTH0_API_BASE_URL')
AUTH0_ACCESS_TOKEN_URL = os.getenv('AUTH0_ACCESS_TOKEN_URL')
AUTH0_AUTHORIZE_URL = os.getenv('AUTH0_AUTHORIZE_URL')