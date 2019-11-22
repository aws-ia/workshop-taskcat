+++
title = "Create Psuedo Parameters"
chapter = false
weight = 210
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

* Note: For the purposes of this lab, we've created a shortcut command to access to the 
file, in the IDE terminal type:

```bash
open-taskcat-global-config
```

The file will contain an empty **general** section when you open it. Let's add an 
override to it for our LicenseToken. notice that the IDE has auto-complete, and 
validation on the config file format, so if anything is invalid you will see it inline, 
and in the **PROBLEMS** tab to the left of the terminal. Once you're done your config 
should look like this:

```yaml
    general:
      parameters:
        LicenseToken: 're:invent-2019-is-awesome'
```

{{% notice warning %}}
Be sure to save the file (Ctrl+s) before closing it
{{% /notice %}}