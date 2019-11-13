+++
title = "- Defining tests"
chapter = false
weight = 14
+++



## Adding test definitions

* Define a test called `mytest` and define the `template` location

* Specfiy path to your relative to you project root `template:` `templates/lab1.template.yaml`

> Optionally you you can set the project_root to a diffrent location if need be:

> `-p PROJECT_ROOT` or  `--project-root PROJECT_ROOT`


```
tests:
  mytest:
    template: templates/lab1.template.yaml
```
