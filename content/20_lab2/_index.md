+++
title = "Lab 2"
chapter = false
weight = 20
+++

## What you will do in this lab:
Using the provided clouformation template build a taskcat config that uses **psuedo-parameters**

We will use override to inject a `LicenseToken` and dynamically inject `AvailiblityZone` 
values during testing

- Use taskcat overrides pass inputs into the stack that you do not want in the 
project_root/gitrepo _(secrets like `LicenseKeys` or `APITokens`, etc. Or account specific 
values like EC2 KeyPair names, or Rooute53 domain names)_

- **psuedo-parameters** can be used to inject dynamic values _(like 
a defined number of Availability Zones for a particular region, random strings, or S3 bucket names)_


To get started navigate to the `lab2/cfn-project` folder in your IDE.
