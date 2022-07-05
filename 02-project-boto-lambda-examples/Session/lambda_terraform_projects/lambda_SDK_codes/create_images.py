import boto3
from datetime import datetime

# Define UTC time zone
now = datetime.now()
time = now.strftime("%m-%d-%Y  %H-%M-%S")

# Define Variables and Configuratios
ec2_client = boto3.client(service_name='ec2', region_name='us-east-1')
regions = ec2_client.describe_regions()['Regions']
response = ec2_client.describe_instances()

# Create Images For Available Instances
def create_images(response):
    for reservation in response['Reservations']:
        for instances in reservation['Instances']:
            instance_id = instances['InstanceId']
            current_time = time
            image_ids=[]
            name = "App_AMI_{instance_id}_{current_time}".format(instance_id=instance_id,current_time=current_time)
            print("Creating image for instance {instance_id}".format(instance_id=instance_id))
            response = ec2_client.create_image(InstanceId=instance_id,Name=name,NoReboot=True, DryRun=False)
            image_ids.append(response['ImageId'])
            print("Image Ids are",image_ids)

    waiter = ec2_client.get_waiter('image_available')
    waiter.wait(ImageIds=image_ids)
    print("Images has been created")

create_images(response)


#TagSpecifications=[{'ResourceType': 'image','Tags': [{'Key': 'string','Value': 'string'}]}]