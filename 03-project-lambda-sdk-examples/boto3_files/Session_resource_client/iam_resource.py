import boto3

aws_profile = boto3.session.Session(profile_name = "botoUserTest") # Session

iam_resource = aws_profile.resource (service_name = 'iam') 

# Listing iam users with resource obect:

for each in iam_resource.users.all():
    print(each.name) 