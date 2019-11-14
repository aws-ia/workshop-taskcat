+++
title = "View test and code promotion"
chapter = false
weight = 52
+++

Now, after your stack creation is completed successfully and you have a CICD pipeline setup, let's see what does the pipeline do.

### View CICD pipeline

On your Cloudformation console, click the **Outputs** tab.

![stack-completed](/images/stack-completed.png)

Look for **CodePipelineURL**, and open the link in a new tab in your browser. 

![pipeline-url](/images/pipeline-url.png)

This will open the AWS Code Pipeline console, and you should see a pipeline.

![pipeline](/images/pipeline.png)

You may see that, either the **Source** action or the **Build** action is in-progress. This is because, when the code pipeline is created for the first time, it automatically gets triggered and start the pipeline execution. 

The **Source** action of the pipeline takes the code from the AWS Code Commit repository and puts it into an S3 bucket. This S3 bucket acts as a source for the next stage of the pipeline, which is **Build** stage.

In **Build** stage, pipeline is using AWS CodeBuild to run TaskCat for your project. It performs all the tests, as defined in the project configuration file. On success, it merges the source branch into the target/release branch.

### Validate code promotion

After the pipeline execution is completed successfully, you should have all the changes committed to the source (develop) branch, available in target/release (master) branch. Let's validate it.

Go to your code commit repository by clicking the following link.

[Code Commit repo](https://us-west-2.console.aws.amazon.com/codesuite/codecommit/repositories/quickstart-ci-repo/commits?region=us-west-2)

Select the branch name from the top right corner, and you should see that your **master** branch has same commits as your **develop** branch.

[TODO:Code commit repository]

**Congratulations!!** You have successfully setup a CICD pipeliine for your CloudFormation project. 

### Summary

You learnt how to setup and use a CICD pipeline for your CloudFormation project, to continously test and deploy your CloudFormation templates.
