import boto3

aws_console = boto3.session.Session(profile_name='botoUser')

ec2_resource = aws_console.resource(service_name='ec2', region_name='us-east-2')

ec2_client = aws_console.client(service_name='ec2', region_name='us-east-2')

#===================== List all Instances ===============================================
# list all instance ids
all_instances_ids=[]       #create a variable to append the result
print("List all instance ids")
for each_instanceID in ec2_resource.instances.all():
    #print(each_instanceID)
    all_instances_ids.append(each_instanceID.id)

print(all_instances_ids)

#========================== Start all instance (Collections and waiters concept)=========
waiter = ec2_client.get_waiter('instance_running') 
print("Starting all instances ......")
ec2_resource.instances.start()  #action 
waiter.wait(InstanceIds=all_instances_ids)
print("All instances are up and running")