import boto3

aws_console_sts = boto3.session.Session(profile_name='botoUser')

sts = aws_console_sts.client(service_name='sts', region_name='us-east-1')
#========================================================================

response = sts.get_caller_identity()

print(response.get('Account'))