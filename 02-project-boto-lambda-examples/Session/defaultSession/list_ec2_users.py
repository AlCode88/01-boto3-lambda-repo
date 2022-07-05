import boto3

ec2_resource = boto3.resource(service_name='ec2', region_name="us-east-1")

for each_instance in ec2_resource.instances.all():
    print(each_instance.id, each_instance.state)