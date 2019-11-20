+++
title = "Deploy CI/CD pipeline"
chapter = false
weight = 520
+++

Now, it's time to setup a CICD pipeline for your project. To do that, go to your team's 
dasbhoard and make a note of the following values. You will need this to create the 
pipeline.

- Your AWS Code Commit **repository Url** (https://)
- Your AWS Code Commit **repository name** - `quiz app`

### Launch stack
To create a CICD pipeline, you will use a CloudFormation template. Click the following 
button to launch a stack creation for the CICD pipeline.

[![launch-stack](/images/launch-stack.png?height=25px)](https://us-west-2.console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=CICD-TCatv9&templateURL=https://aws-quickstart.s3.amazonaws.com/quickstart-taskcat-ci/templates/taskcat-ci-pipeline.yaml.template)

This will open a CloudFormation console in a new tab of your browser, with 
CloudFormation template S3 path pre-populated.

![template-url](/images/template-url.png)

Click **Next**, and fill in the parameter values for **Repository name** and 
**Repository URL**. Leave rest of the parameter values, as default.

After you have provided the parameter values, click **Next**, and **Next** again.

On the *Review* page, scroll down, select the checkboxes for **IAM_CAPABILITIES** and 
click **Create stack**.

![iam-capabilities](/images/iam-capabilities.png)

This will start the stack creation. It will take approximately **5 mins** to finish.
