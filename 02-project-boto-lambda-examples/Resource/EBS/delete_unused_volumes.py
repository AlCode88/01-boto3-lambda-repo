import boto3

def delete_volume():
    ec2_volumes = boto3.resource(service_name='ec2', region_name='us-west-2')
    ebs_unused = {"Name":"status", "Values":["available"]}
    
    for each_volume in ec2_volumes.volumes.all():
        print(each_volume.id, each_volume.state)
        
#     for each_volume_ebs in ec2_volumes.volumes.filter(Filters=[ebs_unused]):
#         print(each_volume_ebs.id, each_volume_ebs.state,each_volume_ebs.tags)
#         print("Deleting unused volumes")
#         each_volume_ebs.delete()
# print("Deleted unused untagged ebs volumes")
delete_volume()

# ec2 = boto3.resource('ec2', region_name='us-east-2')
# volumes = ec2.volumes.all() # If you want to list out all volumes
# volumes = ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['in-use']}]) # if you want to list out only attached volumes
# [volume for volume in volumes]

