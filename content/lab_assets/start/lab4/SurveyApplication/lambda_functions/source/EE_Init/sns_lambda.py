import json
import os
import boto3

MODULE_NAME = os.environ['MODULE_NAME']
DYNAMO_TABLE_ARN = os.environ['DYNAMO_TABLE_ARN']
INIT_LAMBDA = os.environ['INIT_LAMBDA']


def lambda_handler(event, _):

    message = event['Records'][0]['Sns']['Message']
    sns_values = json.loads(message)

    if sns_values['event'] == 'MODULE_DEPLOYED':
        lambda_client = boto3.client('lambda')
        lambda_invoke_response = lambda_client.invoke(
            FunctionName=INIT_LAMBDA,
            InvocationType='Event',
            Payload=json.dumps({'team_id': sns_values['team-id']})
        )
        print(lambda_invoke_response)
