+++
title = "Getting Started"
chapter = false
weight = 50
+++


## What is taskcat?
**taskcat** is a tool to test AWS CloudFormation templates. It deploys your AWS 
CloudFormation template in multiple AWS Regions and generates a report with a pass/fail 
grade for each region. You can specify the regions and number of Availability Zones you 
want to include in the test, and pass in parameter values for your AWS CloudFormation 
template. taskcat is implemented as a cli and a Python class that you can use in your 
own applications.

taskcat was developed by the [AWS Quick Start](https://aws.amazon.com/quickstart/) team to test AWS CloudFormation templates in multiple regions
that automatically deploy workloads on AWS. We’re pleased to make the tool available to 
all developers who want to validate their custom AWS CloudFormation templates across AWS 
Regions.

### Concepts and features

We will cover following concepts and features of taskcat in this workshop:

#TODO - instead of listing features, we should explain what each feature is about. 

- Config hierarchy
- Project config
- Global config
- Parameter overrides
- (Psuedo) parameters
