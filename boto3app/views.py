from pymongo import MongoClient
from datetime import datetime
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from boto3.session import Session
import os
import environ
from .serializers import ProfileImageSerializer, CoverImageSerializer


# Create your views here.

# connection_string = os.environ.get('MONGO_DB_CONNECTION_STRING')
# client = MongoClient('connection_string')
# db = client['NG-STABLE']
# collection_name = db["MERCHANTS"]

# profile_image = collection_name.find({})
# for r in profile_image:
#     print(r['profile_photo'])

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join('.env'))

class UploadProfileImage(generics.GenericAPIView):
    serializer_class = ProfileImageSerializer
    parser_classes = (MultiPartParser,)
    
    def patch(self, request, format=None):
        user = request.user
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            image_extension = os.path.splitext(str(request.data['profile_image']))[1]
            image_name = datetime.now().strftime("%d-%m-%YT%H:%M:%S") + image_extension
            session = Session(region_name=env('AWS_S3_REGION_NAME'), aws_access_key_id=env('AWS_ACCESS_KEY_ID'), aws_secret_access_key=env('AWS_SECRET_ACCESS_KEY'))
            s3 = session.resource('s3')
            # s3.meta.client.upload_file(image_name, env('AWS_STORAGE_BUCKET_NAME'), Key=request.data['profile_image'], ExtraArgs={'ACL': "public-read"})
            s3.Bucket(env('AWS_STORAGE_BUCKET_NAME')).put_object(Key=image_name, Body=request.data['profile_image'],
                                                                 ACL='public-read')
            
            return Response({"message": "Successful"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UploadCoverImage(generics.GenericAPIView):
    serializer_class = CoverImageSerializer
    parser_classes = (MultiPartParser,)
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            image_extension = os.path.splitext(str(request.data['cover_image']))[1]
            image_name = datetime.now().strftime("%d-%m-%YT%H:%M:%S") + image_extension
            session = Session(region_name=env('AWS_S3_REGION_NAME'), aws_access_key_id=env('AWS_ACCESS_KEY_ID'), aws_secret_access_key=env('AWS_SECRET_ACCESS_KEY'))
            s3 = session.resource('s3')
            s3.Bucket(env('AWS_STORAGE_BUCKET_NAME')).put_object(Key=image_name, Body=request.data['cover_image'])
            
            return Response({"message": "Successful"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)