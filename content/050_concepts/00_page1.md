+++
title = "Config hierarchy"
chapter = false
weight = 60
+++


Taskcat uses two config files: _**Global config**_  and _**Project config**_

## Project Config
This config file provides project-specific configurations.

The project config file is located in the root of your project folder **\<PROJECT_ROOT\>/.taskcat.yml**

Since each lab uses the **cfn-project** directory as the _project root_, this is where your project-specific taskcat config file will reside.

## Global config
This config file provides global settings that become defaults for **all projects**.

The global config file is located in user's home-directory.  **~/.taskcat.yml**

{{% notice info %}}
The project-level configuration takes precedence over any items in the global config. However, Global parameters take precedence over project-level parameters. See the next section for more details
{{% /notice %}}
