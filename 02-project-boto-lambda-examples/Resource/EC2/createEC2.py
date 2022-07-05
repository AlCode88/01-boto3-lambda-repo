import boto3

# Create Insance with Boto3
# def create_ec2_instance():
#     try:                                    # try ....exception statement
#         print("Creating EC2 instance")
#         resource_ec2=boto3.client('ec2')
#         resource_ec2.run_instances(         #run_instance is the functio in boto3
#             ImageId="ami-0b9064170e32bde34",
#             MinCount=1,
#             MaxCount=1,
#             InstanceType="t2.micro",
#             KeyName="TalantsMacKey"
#         )
#     except Exception as e:
#         print(e)

# create_ec2_instance()


# Describe Instance with boto3
def describe_instance():
    try:                                                                                    # try ....exception statement
        print("Printing Instance Info")
        resource_ec2=boto3.client('ec2')
        print(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])  #run_instance is the functio in boto3
              
        return str(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
    except Exception as e:
        print(success)

describe_instance()

# Reboot the istance
def reboot_ec2():
    try:
        print("EC2 instance reboot")
        reboot_instance_id = describe_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.reboot_instances(InstanceIds=[reboot_instance_id]))
        print("Instance Rebooting completed")
    except Exception as e:
        print(e)

reboot_ec2()

# Stop the instance
def stop_instance():
    try:
        print("Stopping Instance")
        stop_instance_id = describe_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.stop_instances(InstanceIds=[stop_instance_id]))
    except Exception as e:
        print(e)

stop_instance()