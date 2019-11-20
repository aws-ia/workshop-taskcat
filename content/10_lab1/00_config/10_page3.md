+++
title = "Define project section"
chapter = false
weight = 13
+++



## Add a project section
for the value of `name:` set it to the name of the project folder (**cfn-project**)

> Note: the project name "cfn-project" has been set as the default for the S3KeyPrefix 
> parameter in the provided template, using this pattern your templates are easily re-usable
> in other projects where the project name may differ. If you choose a different name for 
> your project you will need to either update the S3KeyPrefix parameter in the template 
> or set an additional parameter override. Overrides are covered in the next section of this lab

```
project:
  name: cfn-project
```




