import sys
import boto3
import botocore 
# imprt sys  example of syntax error 

# import botoo3   - example of Runtime error

'''
try:
    import botoo3
except Exception as e:
    print(e)


try:
    import botoo3
except ModuleNotFoundError:
    print("Boto3 Module not found. Please install boto3 and try again")
    sys.exit(1)

except Exception as e:
    print(e)
    sys.exit(1)
''' 

try:
    aws_console = boto3.session.Session(profile_name='dev')
except botocore.exceptions.ProfileNotFound:
    print("Dev profile is not found please configure profile name")
    sys.exit(3)