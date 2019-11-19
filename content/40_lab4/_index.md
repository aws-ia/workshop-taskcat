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

In this lab, we'll use taskcat's **--no-delete** flag, which will retain the CloudFormation stack after the test is complete.

To get started, navigate to the `lab4/cfn-project` folder in your IDE
