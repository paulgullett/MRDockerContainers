import boto3
from urllib.parse import unquote_plus

s3_client = boto3.client('s3')
ecs_client = boto3.client('ecs')


def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])

    response = ecs_client.run_task(
        cluster='MRVideoProcessor',
        launchType='FARGATE',
        taskDefinition='MRVideoProcessingTask:1',
        count=1,
        platformVersion='LATEST',
        networkConfiguration={
        'awsvpcConfiguration': {
            'subnets': [
                'subnet-19cee651',
            ],
            'securityGroups': [
                'sg-0dd79259ef86e8905',
            ],
            'assignPublicIp': 'ENABLED'
        }
    },
        overrides={
            'containerOverrides': [
                {
                    'name': 'MRVideoProcessingContainer',
                    'command' : ["/root/bin/fileprocess", key]
                }
            ]
        })

    return str(response)
