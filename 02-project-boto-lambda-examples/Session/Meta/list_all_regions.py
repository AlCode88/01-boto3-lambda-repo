import boto3

aws_console = boto3.session.Session(profile_name='botoUser')

ec2_resource = aws_console.resource(service_name='ec2', region_name='us-east-1')

# print(dir(ec2_resource.meta.client)) will print all availble operations under client

# print(ec2_resource.meta.client.describe_regions()) will print all available regions

# print(ec2_resource.meta.client.describe_regions()['Regions'])

for each_item in ec2_resource.meta.client.describe_regions()['Regions']:
    print(each_item['RegionName'])
    print('=====================')