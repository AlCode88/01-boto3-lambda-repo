import boto3

aws_console = boto3.session.Session(profile_name='botoUser')

ec2_resource = aws_console.resource(service_name='ec2', region_name='us-east-2')

ec2_client = aws_console.client(service_name='ec2', region_name='us-east-2')

#======================== List all prod instances using resource =====================================
'''
prod_instances_resource = []
print("List all prod instances with resource .......")

filters = {"Name": 'tag:env', "Values":['prod']}

for each_prod_instance in ec2_resource.instances.filter(Filters=[filters]):
    prod_instances_resource.append(each_prod_instance.id)

print (prod_instances_resource)
print ("============================")
'''

#========================= List all instances using client ===========================================
#filters_env = {"Name": 'tag:env', "Values":['prod']}
filters_enesai = {"Name": 'tag:Name', "Values":['enesai']}


prod_instances_client = []

#print("List all prod instances with client .......")
print("List all prod instances with enesai tag .......")

for each_instance_client in ec2_client.describe_instances(Filters=[filters_enesai])['Reservations']:
    #print(each_instance_client)
    for each_in_client in each_instance_client['Instances']:
        #print(each_in_client['InstanceId'])
        prod_instances_client.append(each_in_client['InstanceId'])
print(prod_instances_client)


#============================= Stop EC2 isntance ============================================
# print("Stopping instances: ",prod_instances_client)
# ec2_client.stop_instances(InstanceIds=prod_instances_client)
# waiter = ec2_client.get_waiter('instance_stopped')
# waiter.wait(InstanceIds=prod_instances_client)
# print("Your instances are stopped......")

#============================== Start EC2 Instances ==========================================
#print("Starting instances with ids of: ",prod_instances_client)
#ec2_client.start_instances(InstanceIds=prod_instances_client)
#waiter = ec2_client.get_waiter('instance_running')
#waiter.wait(InstanceIds=prod_instances_client)
#print("Your instances are up and running.......")


#============================== Terminate EC2 Instances ======================================
# print("Stopping instances: ",prod_instances_client)
# ec2_client.terminate_instances(InstanceIds=prod_instances_client)
# waiter = ec2_client.get_waiter('instance_terminated')
# waiter.wait(InstanceIds=prod_instances_client)
# print("Your instances are terminated......")