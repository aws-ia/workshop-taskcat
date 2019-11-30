+++
title = "Define parameters"
chapter = false
weight = 150
+++

You can pass parameter values to your template through taskcat configuration file. These values will be passed to your template when launching the stack.

## Add a parameter section to the test

Add the **parameters** key to **mytest**, and set the value of S3BucketName to `$[taskcat_autobucket]`. 

```yaml
parameters: 
  S3BucketName: '$[taskcat_autobucket]'
```

*$[taskcat_autobucket]* is a pseudo-parameter. This tells taskcat to automatically generate an S3 bucket name, create that bucket and use it for test execution.

{{% notice tip %}}
Parameter vaules can be dynamically passed to a stack during creation when testing with taskcat. For example: By specifing **$[taskcat_autobucket]** as the value of **S3BucketName** we are instructing taskcat to replace value with the name of the bucket that will be created at runtime.
{{% /notice %}}
At this time, your *.taskcat.yml* file should look as below.

```yaml
project:
  name: cfn-project
tests:
  mytest:
    template: templates/lab1.template.yaml
    regions:
    - "us-east-1"
    parameters: 
      S3BucketName: '$[taskcat_autobucket]'
```

