#!/usr/bin/env python
"""
Function to generate a random string
author: avattathil@gmail.com
license: Apache 2.0
"""

import random
import string

from crhelper import CfnResource

CRHELPER = CfnResource()


"""
Run on Create and Update
"""


@CRHELPER.create
@CRHELPER.update
def _generate_random_string(event, _):

    if event["ResourceProperties"]["Length"] is not None:
        _length = int(event["ResourceProperties"]["Length"])

    else:
        _length = 8

    _seed = f"{string.ascii_letters}{string.digits}"
    _generated_string = "".join(random.choice(_seed) for x in range(_length))

    CRHELPER.Data["RandomString"] = _generated_string


"""
No delete operation is needed for this program
"""


@CRHELPER.delete
def no_op(_, __):
    pass


"""
handler main
"""


def handler(event, context):
    CRHELPER(event, context)
