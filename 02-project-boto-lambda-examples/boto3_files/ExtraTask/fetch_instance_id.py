import boto3

# List all isntances Id's

instance = boto3.client(service_name='ec2', region_name = 'us-east-1')
#   print (instance.describe_instances()) this is how you describe all the intances

response = instance.describe_instances() # This is the otherway of describing the intance
# print(response)

for each_reservation in response['Reservations']:
    #print (each_reservation)
    for each_instance in each_reservation['Instances']:
        print(each_instance['InstanceId'])