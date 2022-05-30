from configparser import MissingSectionHeaderError
from pymongo import MongoClient
from decouple import config
import logging
import boto3
from botocore.exceptions import ClientError
import os
from boto3.session import Session


connection_string = config('MONGO_DB_CONNECTION_STRING')

myclient = MongoClient(connection_string)
db = myclient.get_database('NG-STABLE')
# my_col = db["MERCHANTS"]

query = {'msisdn': '2348068907955'}

my_doc = db.MERCHANTS.find(query)

for x in my_doc:
    if my_doc:
        print(x)
    else:
        print('No documents found')

# connection_string = config('MONGO_DB_CONNECTION_STRING')
# # print(connection_string)
# client = MongoClient(connection_string)
# db = client['NG-STABLE']
# # print(db)
# collection_name = "MERCHANTS"

# profile_image = db.MERCHANTS.find({"msisdn": '2348068907955'})
# if profile_image:
#     print(profile_image)
# else:
#     print('false')
# for x in profile_image:
#     ajua_details = x.get('collaborators')
#     if 'msisdn' in ajua_details and 'msisdn' == :
#         print('msisdn')
#     else:
#         print('none')
    
    # print(ajua_details)
    # if ' in ajua_details:
    #     cover_photo = ajua_details.get('cover_photo')
    #     print(cover_photo)
    # else:
    #     print('No cover_photo')
        
# bucket_name = config('AWS_STORAGE_BUCKET_NAME')
        
# def upload_cover_image(file_name, bucket, object_name=None):
#     bucket = bucket_name
#     if object_name is None:
#         object_name = os.path.basename(file_name)
        
    # s3 = boto3.resource('s3')
    # s3.meta.client.upload_file(cover_photo, bucket, 'aws_file_name.html', ExtraArgs={'ACL': "public-read"} )
    
    # session = Session(region_name=config('AWS_S3_REGION_NAME'), aws_access_key_id=config('AWS_ACCESS_KEY_ID'), aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'))    
    # s3_client = session.client('s3')
    
    # try:
    #     s3_client.upload_file(cover_photo, bucket, ExtraArgs={'ACL': 'public-read'})
    # except ClientError as e:
    #     logging.error(e)
    #     print(False)
    # print(True)

