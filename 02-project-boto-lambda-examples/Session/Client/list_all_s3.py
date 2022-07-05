import boto3

s3_console = boto3.session.Session(profile_name='botoUser')

s3 = s3_console.client(service_name='s3', region_name='us-east-1')

list_s3_buckets = s3.list_buckets()

# print(list_s3_buckets)

for each_list_s3 in list_s3_buckets['Buckets']:
    print(each_list_s3['Name'])