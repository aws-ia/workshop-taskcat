+++
title = "Create Psuedo Parameters"
chapter = false
weight = 21
+++

## Add Psuedo-Parameters to your project-level taskcat config

* Edit your `cfn_project/.taskcat.yml` parameters to include psuedo-parameters.
[Please see the Taskcat Concepts section for more details on psuedo-parameters](../00_concepts.html)

* Note: Parameter values we want to override from the global config _must still be defined within the project config_. In our example, below, you see a placeholder value. This can be any string and has no other consequence.
* Example project config file:

```
project:
      name: cfn-project
tests:
      mytest:
        template: templates/lab2.template.yaml
        regions:
        - us-east-1
        parameters:
          S3BucketName: '$[taskcat_autobucket]'
          S3KeyPrefix: 'cfn-project/'
          LicenseToken: 'value-to-be-overriden-by-global-config'
          AvailablityZones: $[taskcat_genaz_2]
```

## Add Psuedo-parameters to your global taskcat config.

* Edit your <FILE> parameters to include psuedo-parameters.

* _Note: For the purposes of this lab, we've created a shortcut (symlink) to the actual file_

* Example global config file:

```
general:
      parameters:
        LicenseToken: 're:invent-2019-is-awesome'
```
