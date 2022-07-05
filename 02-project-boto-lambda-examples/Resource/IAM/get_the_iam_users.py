import boto3

iam_console = boto3.session.Session(profile_name='botoUser')

iam_resource = iam_console.resource(service_name='iam', region_name='us-east-1')

# List all users. dir will print all the available methods for iam

# for each_iam in iam_resource.users.all():
#     print(dir(each_iam))

for each_item in iam_resource.users.all():
    print(each_item.name)