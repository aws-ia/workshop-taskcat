+++
title = "Lab 2"
chapter = false
weight = 20
+++

#What you will do in this lab:
Using the provided clouformation template build a taskcat config that uses **psuedo-parameters**

We will use override to inject a `LicenseToken` and dymamically inject `AvailiblityZone` values during testing

The overrides feature can are used to pass input to the that you do not want in the project_root/gitrepo (secrets like license keys or API tokens, etc)

The psuedo-parameters can be used to inject region specfic value (like AvailiblityZone KeyPairNames AccessCIDRs, etc)


Hint: Consider cfn_project under lab2 as the root of your Cloudformation project
