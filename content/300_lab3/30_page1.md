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
        - "us-east-2"
        - "us-west-2"
        parameters:
          S3BucketName: '$[taskcat_autobucket]'
          S3KeyPrefix: 'cfn-project/'
          LicenseToken: 'MY-FAKE-LICENSE-KEY'
          AvailabilityZones: '$[taskcat_genaz_2]'

```

## Test the new regions

```
cd /workshop/lab3/cfn-project
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

To open `taskcat_outputs/index.html` in the AppStream browser, we've provided a simple 
shortcut that can be executed from the terminal:

```
open-taskcat-report
```

![fig1.3](/images/fig_lab1.3.png)

To see the test logs click the **View Logs** link


@TODO: SCREENSHOT OF A FAILURE (INDEX)


@TODO: SCREENSHOT OF SPECIFIC LAMBDA S3 ERROR (IN CFN LOG OUTPUT)
