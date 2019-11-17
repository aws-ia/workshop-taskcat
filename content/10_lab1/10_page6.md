+++
title = "- Define parameters"
chapter = false
weight = 16
+++

## Add a parameter section to the test

* add the `parameters:` set the value of S3BucketName to `$[taskcat_autobucket]` This 
will evaluate to the bucket that taskcat creates during execution.

> Hint: `Parameter vaules can be dynamically passed to a stack during creation when 
>testing with taskcat. For example: By specifing $[taskcat_autobucket]` as the value 
>of `S3BucketName` we can instruct taskcat to replace value with the name of the bucket 
>that will be created at runtime.

```
tests:
  mytest:
    template: templates/lab1.template.yaml
    regions:
    - us-east-1
    parameters: 
      S3BucketName: '$[taskcat_autobucket]'
```

