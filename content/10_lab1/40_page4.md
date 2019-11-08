+++
title = "Add a test section"
chapter = false
weight = 40
+++



## Add a test section

* define a test `mytest`

* specfiy the name of your `template:` `lab1.template.yaml`

* define the `region:` you want to test (for now just specifiy one) `us-east-1`

* add the `parameters:` this template does not require any parameters so just `{}` (to specify no params) 

```
tests:
  mytest:
    template: workshop.yaml
    regions:
    - us-east-1
    parameters: {}

```




