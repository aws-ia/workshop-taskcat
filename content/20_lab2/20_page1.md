+++
title = "Create Psuedo Parameters"
chapter = false
weight = 21
+++

## Add Psuedo-Parameters to your project-level taskcat config

* Edit your `cfn_project/.taskcat.yml` parameters to include psuedo-parameters.
[Please see the Taskcat Concepts section for more details on psuedo-parameters](../00_concepts.html)

* Example project config file:

```yaml
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
      AvailabilityZones: '$[taskcat_genaz_2]'
```

## Add Psuedo-parameters to your global taskcat config.

* Edit your <FILE> parameters to include psuedo-parameters.

* _Note: For the purposes of this lab, we've created a shortcut command to access to the 
file, in the IDE terminal type:

```bash
open-taskcat-global-config
```

* Example global config file:

```yaml
general:
  parameters:
    LicenseToken: 're:invent-2019-is-awesome'
```
