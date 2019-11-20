+++
title = "Defining tests"
chapter = false
weight = 130
+++



## Adding test definitions

* Define a test called `mytest` and define the `template` location

* Specify path to your relative to you project root `template:` `templates/lab1.template.yaml`

> Most of the defaults in taskcat can be overriden with command line flags, the default 
> project root is the current working directory, and the default location for the .taskcat.yml 
> file is in the root. To override these defaults you can use `--project-root PROJECT_ROOT` 
> and `--input-file PATH_TO_/.taskcat.yml` 


```
tests:
  mytest:
    template: templates/lab1.template.yaml
```
