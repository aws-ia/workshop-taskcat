import random
import json
import cfnresponse
from cfnresponse import send, SUCCESS

def handler(event, context):
   if event['RequestType'] == 'Delete':
       send(event, context, 'SUCCESS', {})
       return
   if event['RequestType'] == 'Create':
       token= "%0x%0x" % (random.SystemRandom().getrandbits(3*8),random.SystemRandom().getrandbits(8*8))
       responseData = {}
       responseData['Data'] = token
       send(event, context, 'SUCCESS', responseData)
       return token
