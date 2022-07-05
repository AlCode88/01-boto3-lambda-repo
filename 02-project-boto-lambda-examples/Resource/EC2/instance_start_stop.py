# Lets create EC2 instances using Python BOTO3
import boto3

aws_console = boto3.session.Session(profile_name = 'botoUser')

ec2_client =aws_console.client(service_name ='ec2', region_name ='us-east-1')

def create_ec2_instance():
    """
    MaxCount=1, # Keep the max count to 1, unless you have a requirement to increase it
    InstanceType="t2.micro", # Change it as per your need, But use the Free tier one
    KeyName="ec2-key" # Change it to the name of the key you have.
    :return: Creates the EC2 instance.
    """
    try:
        print ("Creating EC2 instance")
        ec2_client.run_instances(
            ImageId="ami-01cc34ab2709337aa",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="talantsMackey"
        )
    except Exception as e:
        print(e)
create_ec2_instance()


def describe_ec2_instance():
    try:
        print ("Describing EC2 instance")
        print(ec2_client.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        return str(ec2_client.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
    except Exception as e:
        print(e)

describe_ec2_instance()


# def reboot_ec2_instance():
#     try:
#         print ("Reboot EC2 instance")
#         instance_id = describe_ec2_instance()
#         ec2_client = boto3.client("ec2")
#         print(ec2_client.reboot_instances(InstanceIds=[instance_id]))
#     except Exception as e:
#         print(e)


# def stop_ec2_instance():
#     try:
#         print ("Stop EC2 instance")
#         instance_id = describe_ec2_instance()
#         ec2_client = boto3.client("ec2")
#         print(ec2_client.stop_instances(InstanceIds=[instance_id]))
#     except Exception as e:
#         print(e)


def start_ec2_instance():
    try:
        print ("Start EC2 instance")
        instance_id = describe_ec2_instance()
        print(ec2_client.start_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)
start_ec2_instance()


# def terminate_ec2_instance():
#     try:
#         print ("Terminate EC2 instance")
#         instance_id = describe_ec2_instance()
#         ec2_client = boto3.client("ec2")
#         print(ec2_client.terminate_instances(InstanceIds=[instance_id]))
#     except Exception as e:
#         print(e)


#create_ec2_instance()
#describe_ec2_instance()
#reboot_ec2_instance()
#stop_ec2_instance()
#start_ec2_instance()
#terminate_ec2_instance()