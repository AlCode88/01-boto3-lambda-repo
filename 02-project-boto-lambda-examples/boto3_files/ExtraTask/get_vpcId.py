import boto3

permission = boto3.session.Session(profile_name='botoUserTest')

instance = permission.client(service_name='ec2', region_name = 'us-east-1')

response = instance.describe_instances()

for each_reservations in response['Reservations']:
    #print (each_instane['Instances'])
    for each_instance in each_reservations['Instances']:
        print(each_instance['PublicIpAddress'])