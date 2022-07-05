import boto3

aws_console = boto3.session.Session(profile_name='botoUser')

ec2_resource = aws_console.resource(service_name='ec2', region_name='us-east-1')

#========================== List all available volumes =========================

print("List all available volumes.........")

#========================== Variables ==========================================
available_volumes = []
volume_status = {"Name": 'status', "Values":['available']}
volume_name = {"Name": 'tag:Name', "Values":['enesai']}

#=======================================================================================
for volume_resource in ec2_resource.volumes.filter(Filters=[volume_status, volume_name]):
    available_volumes.append(volume_resource.id)

print(available_volumes)
print ("============================")

#========================= Delete all available volumes ===============================
print("Deleting all available volumes...........")
#volume_id=input("Enter volume id that you want to delete: ")
#volumeID = ec2_resource.Volume(available_volumes)
#print(dir(ec2_object))
#print(volumeID)
#print ("Terminating all available EBS Volumes.......")
#volumeID.delete()

for each_volume in available_volumes:
    each_volume.delete()