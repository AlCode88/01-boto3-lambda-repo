import boto3

aws_console = boto3.session.Session(profile_name='botoUser')

ec2_resource = aws_console.resource(service_name='ec2', region_name='us-east-1')

#========================== Variables ==========================================
volume_status = {"Name": 'status', "Values":['available']}

#============================ List all volumes  ================================
print("List all available volumes.........")
for each_volume in ec2_resource.volumes.all():
    print(each_volume.id, each_volume.state, each_volume.tags)
    print("===============================")

#======================== Filter all available isntances ======================================
for each_available_volume in ec2_resource.volumes.filter(Filters=[volume_status]):
    print (each_available_volume)

#======================== Action on EBS volumes ===============================================
for each_volume in ec2_resource.volumes.filter(Filters=[volume_status]):
        print(each_available_volume.id, each_available_volume.state, each_available_volume.tags)
        print("Deleting unused and untagged volumes")
        each_volume.delete()
print("Deleted all unused and untagged volumes................")