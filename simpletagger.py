import boto3

def lambda_handler(event, context):
    ec2=boto3.resource("ec2")
    my_instance_id=event["detail"]["instance-id"]
    my_instance=ec2.Instance(my_instance_id)
    
    my_instance.create_tags(
    Tags=[
        {
            'Key': 'tagged_by_lambda_boto3',
            'Value': 'yes'
        },
    ]
)
    
