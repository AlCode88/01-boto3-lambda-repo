import boto3

s3_client = boto3.client(service_name='s3', region_name='us-east-1')

######### List all buckets with client ### Use paginators with client because you can only list less than 1000 with cleint
all_buckets=[]
for each_s3 in s3_client.list_buckets()['Buckets']:
    all_buckets.append(each_s3['Name'])
print(all_buckets)