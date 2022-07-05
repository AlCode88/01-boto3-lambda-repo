import boto3

iam_res = boto3.resource(service_name='iam', region_name = 'us-east-1')

for each in iam_res.users.all():
    print(each.name)

'''

This is example of custom session

aws_profile = boto3.session.Session(profile_name = "botoUserTest") # Session

iam_resource = aws_profile.resource (service_name = 'iam') 

# Listing iam users with resource obect:

for each in iam_resource.users.all():
    print(each.name)

'''