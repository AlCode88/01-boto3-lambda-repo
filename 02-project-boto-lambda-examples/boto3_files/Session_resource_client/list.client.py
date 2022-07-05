import boto3

aws_profile = boto3.session.Session(profile_name = "botoUserTest")

iam_resource = aws_profile.client(service_name = 'iam', region_name="us-east-1") # Client setup with boto3

# Listing IAM users with client object

for iam_user in iam_resource.list_users()['Users']:
    print (iam_user['UserName']) 