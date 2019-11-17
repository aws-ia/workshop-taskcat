+++
title = "Add additional regions & test"
chapter = false
weight = 41
+++

## Add more regions

* Edit your `lab3/cfn_project/.taskcat.yml` parameters to include additional regions.

* Example project config file:

```
project:
      name: cfn-project
tests:
      mytest:
        template: templates/lab3.template.yaml
        regions:
        - us-east-1
        - us-east-2
        - us-west-1
        parameters:
          S3BucketName: '$[taskcat_autobucket]'
          S3KeyPrefix: 'cfn-project/'
          LicenseToken: 'MY-FAKE-LICENSE-KEY'
          AvailabilityZones: $[taskcat_genaz_2]

```

## Test the new regions

```
taskcat test run
```

## Test Results

After the test completes you will see a new folder under `cfn-project` called **taskcat_outputs**
```
cfn-project
├── lambda_functions
├── templates
├── .taskcat.yml
└── taskcat_outputs/index.html < - (report)

```

open `taskcat_outputs/index.html` in the your web browser
![fig1.3](/10_lab1/images/fig_lab1.3.png)

To see the test logs click the **View Logs** link


@TODO: SCREENSHOT OF A FAILURE (INDEX)


@TODO: SCREENSHOT OF SPECIFIC LAMBDA S3 ERROR (IN CFN LOG OUTPUT)
