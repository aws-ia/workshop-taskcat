import cfnresponse
import traceback
import boto3
from time import sleep


def handler(event, context):
    print(event)
    status = cfnresponse.SUCCESS
    try:
        role_arn = event["ResourceProperties"]["IamRoleArn"]
        appstream = boto3.client("appstream")
        req = event.get("RequestType")
        state = appstream.describe_fleets(Names=["VSCodeFleet"])['Fleets'][0]['State']
        if req == "Create" and state == 'STOPPED':
            appstream.update_fleet(Name="VSCodeFleet", IamRoleArn=role_arn)
            appstream.start_fleet(Name="VSCodeFleet")
            state = 'STARTING'
        if req == "Delete" and state == 'RUNNING':
            appstream.stop_fleet(Name="VSCodeFleet")
            state = 'STOPPING'
        while context.get_remaining_time_in_millis() / 1000 > 35:
            sleep(30)
            state = appstream.describe_fleets(Names=["VSCodeFleet"])['Fleets'][0]['State']
            if (state == 'RUNNING' and req == "Create") or (state == 'STOPPED' and req == "Delete"):
                break
    except Exception:
        traceback.print_exc()
        status = cfnresponse.FAILED
    cfnresponse.send(event, context, status, {})
