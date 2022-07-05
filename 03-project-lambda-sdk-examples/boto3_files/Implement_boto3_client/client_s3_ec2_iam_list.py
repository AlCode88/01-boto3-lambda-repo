import boto3

aws_session_profile = boto3.session.Session(profile_name='botoUserTest') # Custom Session

iam_resource = aws_session_profile.client(service_name = 'iam', region_name = 'us-east-1') # Default Session
ec2_resource = aws_session_profile.client(service_name = 'ec2', region_name = 'us-east-1') # Default Session
s3_resource = aws_session_profile.client(service_name = 's3', region_name = 'us-east-1')   # Default Session

# List all iam users
iam_response = iam_resource.list_users()
for iam_user in iam_response['Users']:
    print(iam_user['UserName'])
    print('------------------')

# List EC2 ids
ec2_response = ec2_resource.describe_instances()
# print(ec2_response['Reservations'])
for ec2_instance_id in ec2_response['Reservations']:
    for instance in ec2_instance_id['Instances']:
        print(instance['InstanceId'])
    print('-------------')

# List Bucket Name
s3_bucket_name = s3_resource.list_buckets()
for s3_bucktes in s3_bucket_name['Buckets']:
    print(s3_bucktes['Name'])