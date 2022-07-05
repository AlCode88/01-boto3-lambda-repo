import boto3
s3 = boto3.resource('s3')

my_bucket = s3.Bucket('tf-state-files-development')

for file in my_bucket.objects.all():
    print(file.key)