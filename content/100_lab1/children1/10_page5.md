+++
title = "Define regions"
chapter = false
weight = 140
+++



## Add regions to your test

* The `region:` key is optional for tests by default region inherit from the global 
configuration (We will conver global configs later in this lab)

The region parameter takes a _list_ of regions. When defined in a  test, taskcat will 
limit test to those regions

For now only specifiy one region `us-east-1`

```
tests:
  mytest:
    template: templates/lab1.template.yaml
    regions:
    - us-east-1
```




