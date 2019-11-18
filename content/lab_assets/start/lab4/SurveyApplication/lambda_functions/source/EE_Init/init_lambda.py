import os

import boto3
from api import EEAPIClient

API_TOKEN = os.environ['EE_API_TOKEN']
MODULE_NAME = os.environ['MODULE_NAME']
EVENT_ID = os.environ['EE_EVENT_ID']
API_BASE = os.environ['EE_API_BASE']
REGION = os.environ['EVENT_REGION']
DYNAMO_TABLE_ARN = os.environ['DYNAMO_TABLE_ARN']

TRUST = """{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "", 
            "Effect": "Allow", 
            "Principal": {"AWS": "%s"}, 
            "Action": "sts:AssumeRole"
        }
    ]
}
"""

POLICY = """{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "WriteOwnItems",
            "Effect": "Allow",
            "Action": ["dynamodb:PutItem"],
            "Resource": ["%s"],
            "Condition": {
                "ForAllValues:StringEquals": {"dynamodb:LeadingKeys": ["%s"]}
            }
        }
    ]
}"""


def lambda_handler(event, _):
    print(event)
    ee_api_client = EEAPIClient(API_BASE, API_TOKEN, EVENT_ID, MODULE_NAME)

    ee_response = ee_api_client.get_one_team(event["team_id"])
    print(ee_response)

    streaming_url = ee_response['modules'][MODULE_NAME]['cfn-outputs']['StreamingUrl']
    cc_url = ee_response['modules'][MODULE_NAME]['cfn-outputs']['CodeCommitUrl']
    cc_user = ee_response['modules'][MODULE_NAME]['cfn-outputs']['CodeCommitUser']
    cc_pass = ee_response['modules'][MODULE_NAME]['cfn-outputs']['CodeCommitPassword']

    ee_api_client.post_output(
        event["team_id"],
        "module_deployed_output",
        "Resources",
        f'---\n\n**Workshop guide:** [workshop.taskcat.io](http://workshop.taskcat.io)\n\n'
        f'**IDE:** [Click here to launch]({streaming_url})\n\n '
        f'---\n\n**DynamoDB ARN:** ```{DYNAMO_TABLE_ARN}```\n\n'
        f'---\n\n**CodeCommit git URL:** ```{cc_url}```\n\n'
        f'**CodeCommit git user:** ```{cc_user}```\n\n'
        f'**CodeCommit git password:** ```{cc_pass}```\n\n',
        0,
        markdown=True,
        description=''
    )

    team_acc_id = ee_response["account"]["account-id"]
    role_name = f"team_{team_acc_id}_role"
    iam = boto3.client("iam", region_name=REGION)
    iam.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=TRUST % team_acc_id
    )
    iam.put_role_policy(
        RoleName=role_name,
        PolicyName='ddb_write',
        PolicyDocument=POLICY % (DYNAMO_TABLE_ARN, team_acc_id)
    )
