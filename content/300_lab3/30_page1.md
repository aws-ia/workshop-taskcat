+++
title = "Add additional regions & test"
chapter = false
weight = 310
+++

## Add more regions

* Edit your `lab3/cfn_project/.taskcat.yml` parameters to include additional regions. 
Below is an example of what your file should look like once you're done.

```
project:
      name: cfn-project
tests:
      mytest:
        template: templates/lab3.template.yaml
        regions:
        - us-east-1
        - us-east-2
        - us-west-2
        parameters:
          S3BucketName: '$[taskcat_autobucket]'
          S3KeyPrefix: 'cfn-project/'
          LicenseToken: 'MY-FAKE-LICENSE-KEY'
          AvailabilityZones: '$[taskcat_genaz_2]'

```

{{% notice warning %}}
Be sure to save the file (Ctrl+s) before running taskcat
{{% /notice %}}

## Test the new regions

```
taskcat test run
```
![fig3.1](/images/taskcat_execution3.gif)
