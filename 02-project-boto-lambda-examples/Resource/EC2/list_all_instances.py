import boto3

ec2_console = boto3.session.Session(profile_name='botoUser')

ec2 = ec2_console.resource(service_name='ec2', region_name='us-east-1')

# for each_ec2 in ec2.instances.all():
#     print(dir(each_ec2))

for each_ec2 in ec2.instances.all():
    print(each_ec2.vpc_id)
    