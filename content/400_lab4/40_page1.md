+++
title = "Run test with no-delete"
chapter = false
weight = 410
+++


## Execute the test. 

* Run **taskcat test run --no-delete** or **-n** flag to retain the CloudFormation stack 

```
cd /workshop/lab4/cfn-project
taskcat test run --no-delete
```

### Launch the application after deployment.

* Once the taskcat test completes, navigate to the CloudFormation console by clicking...

[CloudFormation Console](https://console.aws.amazon.com/cloudformation/home)

TODO: Add screenshort for the survey endpoint
![fig4.1](/images/survey_link.png)
