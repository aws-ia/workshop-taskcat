+++
title = "Deploy CI/CD pipeline"
chapter = false
weight = 51
+++

To setup a CICD pipeline for your project, you need the following details. Make a note of the following before proceeding with the rest of the steps: -

1. Your AWS Code Commit **repository name**
2. Your AWS Code Commit **repository Url** (https://)
3. **Source branch name**, where you will be pushing your changes
4. **Release branch name**, where your changes needs to be promoted, after successfull test

### Launch stack
To create a CICD pipeline, you will use a CloudFormation template. Click the following button to launch a stack creation for the CICD pipeline.
[![launch-stack](/images/launch-stack.png?height=25px)](https://us-west-2.console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=CICD-TCatv9&templateURL=https://aws-quickstart.s3.amazonaws.com/quickstart-taskcat-ci/templates/taskcat-ci-pipeline.yaml.template)

This will open a CloudFormation console in a new tab in your browser, with CloudFormation template S3 path pre-populated.

![template-url](/images/template-url.png)

Click **Next**, and fill in the parameter values with the values you made a note of, earlier. Leave default values for **Quick Start S3 Bucket Name** and **Quick Start S3 Key Prefix** parameters.

After you have provided all the parameter values, click **Next**, and **Next** again.

On the *Review* page, scroll down, select the checkboxes for **IAM_CAPABILITIES** and click **Create stack**.

![iam-capabilities](/images/iam-capabilities.png)

This will start the stack creation. It will take approximately **5 mins** to finish.
