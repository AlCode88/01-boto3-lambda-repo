import boto3

# You need to set the profile, what kind of pemission you would like to use
iam_console = boto3.session.Session(profile_name='botoUser')

# Define Resource or Client
list_iam = iam_console.client(service_name='iam', region_name='us-east-1')

# Define Code
response = list_iam.list_users() # ['User']
# print(response) you can print and check the value first

# The same response
# print(response['Users'])

# You can loop it and take the dictionary out of the list
for each_item in response['Users']:
    print(each_item['UserName'])