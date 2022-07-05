import boto3
s3_resource = boto3.resource(service_name='s3', region_name='us-east-1')
all_buckets=[]
for each_s3 in s3_resource.buckets.all():
    all_buckets.append(each_s3.name)
    object = s3_resource.Object(all_buckets)