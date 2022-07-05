import boto3

def list_instance_id_ami():
    # Profile Name
    ec2_console = boto3.session.Session(profile_name='botoUser')
    
    # Define Client or Resource
    ec2 = ec2_console.client(service_name='ec2', region_name='us-east-1')
    
    response = ec2.describe_instances()
    print(response)
    print('======================')
    
    #print(response['Reservations'])
    
    for each_item in response['Reservations']:
            #print(each_item['Instances'])
            #print('==========================')
        for each_instance in each_item['Instances']:
            print(each_instance['ImageId']) 
            print(each_instance['InstanceId'])
            print('======================') 

list_instance_id_ami()