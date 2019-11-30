from yattag import Doc
import boto3
import os
from datetime import datetime


def acc_id_from_arn(arn):
    return arn.split(":")[4]


def region_from_arn(arn):
    return arn.split(":")[3]


def table_name_from_arn(arn):
    return arn.split("/")[1]


def get_ddb_table(local_acc):
    arn = os.environ['TABLE_ARN']
    ddb_acc = acc_id_from_arn(arn)
    ddb_region = region_from_arn(arn)
    table_name = table_name_from_arn(arn)
    if ddb_acc == local_acc:
        session = boto3.Session()
    else:
        sts_client = boto3.client("sts")
        creds = sts_client.assume_role(
            RoleArn=f"arn:aws:iam::{ddb_acc}:role/team_{local_acc}_role",
            RoleSessionName="survey"
        )['Credentials']
        session = boto3.Session(
            aws_access_key_id=creds['AccessKeyId'],
            aws_secret_access_key=creds['SecretAccessKey'],
            aws_session_token=creds['SessionToken']
        )
    dynamodb = session.resource('dynamodb', region_name=ddb_region)
    return dynamodb.Table(table_name)


def lambda_handler(event, context):
    account_id = acc_id_from_arn(context.invoked_function_arn)
    table = get_ddb_table(account_id)
    timestamp = int(datetime.now().timestamp() * 1000000)
    item_data = {'id': str(account_id), 'timestamp': timestamp}
    for param in event["queryStringParameters"]:
        value = event["queryStringParameters"][param]
        if not value:
            value = "-"
        item_data[param] = value
    table.put_item(
        Item=item_data
    )
    doc, tag, text = Doc().tagtext()
    with tag('html'):
        with tag('body'):
            with tag('div', align='center'):
                with tag('h1'):
                    count = 0
                    while count < 6:
                        count += 1
                        doc.stag('br')
                    text("Your answer was submitted!")
    html_result = doc.getvalue()
    return {
            'statusCode': "200",
            'body': html_result,
            'headers': {
                'Content-Type': 'text/html',
                "Refresh": "5;url=newsurvey",
            }
        }
