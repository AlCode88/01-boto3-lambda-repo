import boto3

aws_console = boto3.session.Session(profile_name='botoUser')

ec2_resource = aws_console.resource(service_name='ec2', region_name='us-east-1')

#===============================================================================

#print(dir(ec2_resource))

volume_in_use = {"Name": "status", "Values":['in-use']}

for volume in ec2_resource.volumes.filter(Filters=[volume_in_use]):
    print(volume)