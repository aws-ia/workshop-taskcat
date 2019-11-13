+++
title = "Deploy CI/CD pipeline"
chapter = false
weight = 10
+++

To setup a CICD pipeline for your project, you need the following details. Make a note of the following before proceeding with the rest of the steps: -

1. Your AWS Code Commit **repository name**
2. Your AWS Code Commit **repository Url** (https://)
3. **Source branch name**, where you will be pushing your changes
4. **Release branch name**, where your changes needs to be promoted, after successfull test

### Create stack
To create a CICD pipeline, you will launch a CloudFormation template.

Click [TODO:LauchStack-button].

This will open a CloudFormation console in a new tab in your browser, with CloudFormation template S3 path pre-populated.

[TODO:Screenshot]

Click **Next**, and fill in the parameter values. Use the values you made a note of, earlier.
Leave default values for **Quick Start S3 Bucket Name** and **Quick Start S3 Key Prefix** parameters.

After you have provided all the parameter values, your page should look like below.

[TODO:Screenshot]

Click **Next**, and **Next** again.

On the *Review parameters* page, scroll down, select the checkboxes for **IAM_CAPABILITIES** and click **Next**.

Click **Create**.

This will start the stack creation. It will take approximately **5 mins** to finish.

[TODO:Scrrenshot]

### View CICD pipeline

After the stack creation is completed successfully, click the **Outputs** tab and look for **CodePipelineURL**.

[TODO:Screenshot]

Press **Ctrl Key** in your keyboard and click the **CodePipelineUrl**. This will open the AWS Code Pipeline console in a new tab on your browser, and you should see a pipeline.

[TODO:Screenshot]

Note: You may see that either the **Source** action or the **Build** action is in-progress. This is because, when the code pipeline is created for the first time, it automatically gets triggered. But don't worry, in the next section we will see the full workflow in-action, starting from making a commit locally, pushing the changes to the code commit reposirotry, and seeing the pipeline being triggered, which then runs the tests and promotes the changes to the release branch, on successfull test.
