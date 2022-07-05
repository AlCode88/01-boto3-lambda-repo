import boto3

s3_console = boto3.session.Session(profile_name='boto-test')

s3 = s3_console.resource(service_name='s3', region_name='us-east-1')

# To list all biuckets in S3 console
# for each_s3 in s3.buckets.all():
#     print(dir(each_s3))

# To list specific number of buckets
for each_s3 in s3.buckets.all():
    print(each_s3.name)