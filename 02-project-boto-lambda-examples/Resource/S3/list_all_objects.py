# list all S3 in your account

import boto3 # import module

s3 = boto3.resource('s3') # Define a resource

for bucket_list in s3.buckets.all():
    print(bucket_list.name)