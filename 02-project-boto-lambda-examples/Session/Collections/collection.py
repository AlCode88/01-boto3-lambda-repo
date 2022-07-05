import boto3

aws_console = boto3.session.Session(profile_name='botoUser')

ec2_resource = aws_console.resource(service_name='ec2', region_name='us-east-1')

# print(dir(ec2_resource.instances))

# print(ec2_resource.instances.all())

#=====================================================
# To list all isntance in your account you can use "all"
#for each in ec2_resource.instances.all():
#     print(each)

#=====================================================
# To limit available isntances that you "list" not really useul but still it is exists
#for each_limit in ec2_resource.instances.limit(1):
#    print(each_limit)


filter = {"Name": "instance-state-name", "Values":['running','stopped']} #you can get the values from

filter2 = {"Name": "instance-type", "Values":['t2.micro','t3.medium']}

for each_filter in ec2_resource.instances.filter(Filters=[filter, filter2]):
    print(each_filter)