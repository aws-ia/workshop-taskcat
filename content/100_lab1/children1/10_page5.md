+++
title = "Define regions"
chapter = false
weight = 140
+++

Now, you will define in which AWS regions you want to test your cloudformation templates.

## Add regions to your test

The **regions:** key is optional for the tests. By default **regions** inherit from the global 
configuration (We will conver global configs later in this lab)

The regions key takes a _list_ of regions. When defined in a  test, taskcat will 
limit test to those regions

For now, specifiy only one region **us-east-1**.

After you have defined tests, your config file should look as below.

```yaml
project:
  name: cfn-project
tests:
  mytest:
    template: templates/lab1.template.yaml
    regions:
    - us-east-1
```




