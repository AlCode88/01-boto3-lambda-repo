import boto3
list_ec2_snaps = boto3.client(service_name='ec2', region_name='us-east-1')

enesai_snaps = {'Name':'tag:Name', 'Values':['enesai']}


response = list_ec2_snaps.describe_instances(Filters=[enesai_snaps])
instance_id = []
for reservation in response['Reservations']:
    for instances in reservation['Instances']:
        instance_id.append(instances['InstanceId'])
print(instance_id)