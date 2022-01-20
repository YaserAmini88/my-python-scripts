#!/usr/bin/python3

import boto3

s3=boto3.resource("s3")
bucket_name="Bucket1"
try:
    response=s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint':'use-east-2'})
    print(response)
except Exception as error:
    print(error)
