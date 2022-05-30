from celery import Celery
import os
import logging
import boto3
from botocore.exceptions import ClientError


app = Celery('tasks', broker='amqp://guest@localhost//', )

@app.task
def reverse(string):
    return string[::-1]

@app.task
def add(x, y):
    return x + y

@app.task
def upload_image(file_name, bucket, object_name):
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
    
    