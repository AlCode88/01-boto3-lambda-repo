import boto3
s3_client = boto3.client(service_name='s3', region_name='us-east-1')
bucket_name = 'terraform-bucket-tb'
print(s3_client.list_objects(Bucket=bucket_name))