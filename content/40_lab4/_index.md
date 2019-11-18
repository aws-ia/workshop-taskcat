+++
title = "Lab 4"
chapter = false
weight = 40
+++

# What you will do in this lab:
In this lab we see how taskcat can be useful in testing an application.  We will deploy 
a pre-configured application via CloudFormation and validate the functionality.

We will learn how to use taskcat to do a local deployment of our app and instruct 
taskcat not to delete the stack at completion using it as a test deployment tool.


## Execute the test.

* In this lab, we'll use the `--no-delete` (or `-n`) flag with `taskcat test run` to 
retain the CloudFormation stack after the test is complete.

`taskcat test run --no-delete`

## Launch the application after deployment.

* Once the taskcat test completes, navigate to the CloudFormation console by clicking...



## Complete the survey
