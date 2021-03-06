import boto3
import os

def lambda_handler(event, context):
    ec2=boto3.resource("ec2")
    instance_id = os.environ.get('INSTANCE_ID')
    my_instance=ec2.Instance(instance_id)

    if my_instance.state['Name'] == "running":
        my_instance.stop()
    elif my_instance.state['Name'] == "stopped":
        my_instance.start()
    
