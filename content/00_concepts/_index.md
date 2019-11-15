+++
title = "Getting Started"
chapter = true
weight = 3
+++


## What is taskcat?
**taskcat** is a tool that tests AWS CloudFormation templates. It deploys your AWS 
CloudFormation template in multiple AWS Regions and generates a report with a pass/fail 
grade for each region. You can specify the regions and number of Availability Zones you 
want to include in the test, and pass in parameter values from your AWS CloudFormation 
template. taskcat is implemented as a cli and a Python class that you can use in your 
own applications.

taskcat was developed by the AWS QuickStart team to test AWS CloudFormation templates 
that automatically deploy workloads on AWS. We’re pleased to make the tool available to 
all developers who want to validate their custom AWS CloudFormation templates across AWS 
Regions

#### taskcat concepts and features we will cover in this lab

- Config hierarchy
- Project config
- Global config
- Parameter overrides
- (Psuedo) parameters
