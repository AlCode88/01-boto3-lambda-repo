import boto3
import sys

ec2_console = boto3.session.Session(profile_name='botoUser')

ec2_resource = ec2_console.resource(service_name='ec2', region_name='us-east-1')

ec2_client = ec2_console.client(service_name='ec2', region_name='us-east-1')

#================================================================================

while True:
    print ("This script perfoms the following actions on ec2 intance")
    print("""
    1. start
    2. stop
    3. terminate
    4. exit
    """)
    opt=int(input("Enter your choice: "))
    
    if opt==1:
        instance_id=input("Enter your EC2 Instance id: ")
        ec2_object = ec2_resource.Instance(instance_id)
        print(dir(ec2_object))
        print("=========================================")
        print ("Starting EC2 instance.......")
        ec2_object.start()
    
    elif opt==2:
        instance_id=input("Enter your EC2 Instance id: ")
        ec2_object = ec2_resource.Instance(instance_id)
        print ("Stopping EC2 instance.......")
        ec2_object.stop()
    
    elif opt==3:
        instance_id=input("Enter your EC2 Instance id: ")
        ec2_object = ec2_resource.Instance(instance_id)
        print ("Terminating EC2 instance....")
        ec2_object.terminate()
    
    elif opt==4:
        print("Exiting, thank you for usig this script")
        sys.exit()
    else:
        print("Your option is invalid please enter correct option")