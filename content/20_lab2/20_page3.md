+++
title = "Check Template Outputs"
chapter = false
weight = 23
+++


## Login to the AWS Console

1. from the [Event Engine dashboard](https://dashboard.eventengine.run/) click login to AWS console
2. navigate to the CloudFormation console in us-east-1 (N. Virginia)
3. Change the filter to view **Deleted** stacks
3. Select the top stack ( they are ordered by creation date)
4. Click on the **"Outputs"** tab

Notice that the values for the **LicenseToken** parameter has been replaced with the value 
specified in the global override.

Notice that the value for **AvailablityZones** has been replaced with 2 az names from the 
us-east-1 region


@TODO: MORE SCREENSHOTS OF TEMPLATE OUTPUTS
