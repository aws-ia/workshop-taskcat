+++
title = "Lab 5"
chapter = false
weight = 500
+++

## Setup CICD pipeline for your project
In this lab, you will learn how to do continuous integration of your CloudFormation 
templates, by creating a CI/CD pipeline for your project.

The following diagram shows what you will deploy in this lab.
![architecture](/images/cicd-pipeline-arch.png)

The CI/CD pipeline uses AWS Codepipeline and AWS Code Build services. AWS Codepipeline 
has a source action for AWS Code commit repository, and a build action uses AWS Code 
Build to run tests. The Code Build runs TaskCat to perform the tests, similar to how 
you run TaskCat locally on your laptop.

After you have set up a CI/CD pipeline for your project, the next time you push any changes 
to your git repository, it will trigger the pipeline. This will run the tests you have 
defined in your project configuration file, and on a successfull test, the changes will 
be promoted from the source branch to the target/release branch.

So, let's get started.

To get started, navigate to the `lab5/cfn-project` folder in your IDE.

