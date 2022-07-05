import boto3

aws_console = boto3.session.Session(profile_name='botoUser')

ec2_resource = aws_console.resource(service_name='ec2', region_name='us-east-1')

#===============================================================================

#print(dir(ec2_resource))

filters = {"Name": 'tag:Name', "Values":['boto3']}
filter_env = {"Name": 'tag:env', "Values":['dev']}


for each_tag in ec2_resource.instances.filter(Filters=[filters, filter_env]):
    print(each_tag)