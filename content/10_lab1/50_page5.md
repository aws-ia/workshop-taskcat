+++
title = "Add inputs to your test "
chapter = false
weight = 40
+++



## Add a parameter section to the test

* define a test `mytest`

* specfiy the name of your `template:` `lab1.template.yaml`

* define the `region:` you want to test (for now just specifiy one) `us-east-1`

* add the `parameters:` set the value of S3BucketName to `$[taskcat_autobucket]` This will evaulate to the bucket that taskcat creates during execution

> Hint: `Parameter vaules can be dynamically passed to a stack during creation when testing with taskcat. For example: By specifing $[taskcat_autobucket]` as the value of `S3BucketName` we can instruct taskcat to replace value with the name of the bucket that will be created at runtime

```
tests:
  mytest:
    template: templates/lab1.template.yaml
    regions:
    - us-east-1
    parameters: 
      S3BucketName: '$[taskcat_autobucket]'
```

