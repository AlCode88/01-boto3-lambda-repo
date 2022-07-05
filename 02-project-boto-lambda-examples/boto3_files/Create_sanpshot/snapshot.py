import boto3

ec2 = boto3.resource(service_name='ec2', region_name='us-east-1')

for instance in ec2.instances.filter(Filters=[{'Name': "instance-state-name",'Values': ["running"]}]):
    for device in instance.block_device_mappings:
        ec2.create_snapshot(VolumeId=device.get('Ebs').get('VolumeId'))
print("Snapshots has been created")