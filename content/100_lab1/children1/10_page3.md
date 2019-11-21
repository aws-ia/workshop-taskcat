+++
title = "Define project section"
chapter = false
weight = 120
+++

First, you will create a project section in your project configuration file.

## Add a project section

To add a project section, copy and paste the following in **.taskcat.yml** file.

```yaml
project:
  name: cfn-project
```

{{% notice warning %}}
It is important that you keep the project name as **cfn-project**. This value is being used in other places in CloudFormation templates, that you will be using in this workshop. Changing the project name may cause issues in future labs.
{{% /notice %}}



