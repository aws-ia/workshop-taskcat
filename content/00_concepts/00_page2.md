+++
title = "Parameter Overrides"
chapter = false
weight = 3
+++

### Parameter Overrides

Parameter Overrides were added to taskcat to solve a couple common problems: first, many 
templates share common parameters that are unique to an AWS account like a KeyPair name 
or an S3 Bucket, overrides provided a way to store those centrally for all your projects. 
Secondly, we didn't want to add sensitive data (usernames, passwords, tokens) to a git 
repository. The idea was to store sensitive/unique data outside of a git repository, but still 
execute a test using this data. To that end, _any parameter defined in the global config 
will take precedence over the same parameter in a project-level config_. 


### (Psuedo) Parameters

To increase the flexibility of taskcat, we've built in support for _psuedo-parameters_ that are transposed at runtime for actual values.

| Psuedo-Parameter | Example Value passed to the CloudFormation stack | Details |
| ------------- | ------------- | ------------- |
| `$[taskcat_autobucket]` | taskcat-tag-sample-taskcat-project-5fba6597 | _Note: The S3 Bucket is created_ |
| `$[taskcat_genaz_1]` | "us-east-1a"  | Fetches a single  Availability Zone within the region being launched in |
| `$[taskcat_genaz_2]` | "us-east-1a,us-east-1b"  | Fetches two AvailabilityZones within the region being launched in |
| `$[taskcat_genaz_3]` | "us-east-1a,us-east-1b,us-east-1c"  | Fetches three AvailabilityZones within the region being launched in |
| `$[taskcat_genpass_8A]`  | tI8zN3iX8 | An alphanumberic 8-charater random password. The length is customizable. |
| `$[taskcat_genpass_8S]`  | mA5@cB5! | An alphanumberic 8-charater random password. The length is customizable. |
| `$[taskcat_random-string]` | yysuawpwubvotiqgwjcu | Generates a random string |
| `$[taskcat_random-numbers]` | 56188163597280820763 | Generates random numbers. |
| `$[taskcat_genuuid]` | 1c2e3483-2c99-45bb-801d-8af68a3b907b | Generates a UUID |


