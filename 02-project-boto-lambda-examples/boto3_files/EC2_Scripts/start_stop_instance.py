import boto3
import sys
#
ec2_client = boto3.resource(service_name='ec2',region_name='us-east-1')

while True:
    print ("This script performs the following actions on EC2 isntance")
    print ("""
           1. Start
           2. Stop
           3. Terminate
           4. Exit"""
    )
    opt=int(input("Enter your option: "))
    
    if opt ==1:
        instance_id=input("Enter your instance ID: ")
        start_ec2 = ec2_client.Instance(instance_id)  # This is the intance Object you can get it from the documentation page in the Service resource section 2. you can get the Instace from the official documentation of boto3 column 2
        print (dir(start_ec2))                        # dir() is the Python built in function. Returns a list of the specified object's properties and methods                      
        print("Starting EC2 instance..........")
        start_ec2.start()
    
    elif opt ==2:
        instance_id=input("Enter your instance ID: ")
        stop_ec2 = ec2_client.Instance(instance_id)
        print("Stopping EC2 instance.......")
        stop_ec2.stop()
    
    elif opt == 3:
        instance_id=input("Enter your instance ID: ")    
        terminate_instance = ec2_client.Instance(instance_id)
        print ("Terminating EC2 instance .......")
        terminate_instance.terminate()
    
    elif opt ==4:
        print ("Thank you for usgin this script")
        sys.exit()
        instance_id=input("Enter your instance ID:  ")
    
    else:
        print("You option is invalid. Please Try again")