import boto3
s3_resource = boto3.resource(service_name='s3', region_name='us-east-1')
bucket_name = 'terraform-bucket-tb'
bucket_object = s3_resource.Bucket(bucket_name)
cnt=1
for each_object in bucket_object.objects.all():
    print(cnt,each_object.key)
    cnt=cnt+1