+++
title = "Build a project from scratch"
chapter = false
weight = 620
+++

Write a template that creates a vpc with a private subnet and deploys an ec2 instance 
into it. This lab will give you insight into the cfn-lint IDE integration, which eases
authoring templates. It also gives you an opportunity to build a taskcat config from 
scratch.

Template should have the following:

* Allow users to provide the subnet CIDR block and AZ name via Parameters.
* Pass taskcat tests in *us-east-1*, *us-west-2* and *eu-west-1*

{{% notice tip %}}
To ensure your stack deploys as quickly as possible, define as few vpc resources as 
possible, NAT gateways in particular can add a few minutes to a vpc deployment
{{% /notice %}}
