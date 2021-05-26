# Flask Test Configuration file
import os
from dotenv import load_dotenv

load_dotenv()


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