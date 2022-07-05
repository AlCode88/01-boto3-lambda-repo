import boto3

ec2 = boto3.client(service_name='ec2', region_name='us-east-1')

response = ec2.run_instances(
   ImageId='ami-04ad2567c9e3d7893',
   InstanceType='t2.micro',
   KeyName='TB_keys',
   MinCount=1,
   MaxCount=1,
   TagSpecifications=[
        {
            'ResourceType':'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'TestBotoInstance'
                }
            ]
        }
    ] 
)

waiter = ec2.get_waiter('instance_running')
print("Your test instance has been crearted")