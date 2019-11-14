+++
title = "Lab 3"
chapter = false
weight = 30
+++

### Testing in multiple region

A important part of building high confidence cloudformation is multi region testing. 

In this lab we will see how **taskcat** can help uncover common issue when deploying in multiple regional.

In this lab we will use the same template which builds a lambda backed customer resource. 

To test this template we will add 2 more regions to the test taskcat config.

- After running the test we will see that will **us-east-1** deploys properly we get failures in the other regions. Looking at the logs we can see that lambda source is not accessable from the other regions. 

- We will then make some modification to the template which correct this issue by adding a nested template which prestages the lambda source. 

- Finally kick off out taskcat test again to validate the fix we implemented!

> Hint: Consider cfn_project under **start/lab3** as the root of your Cloudformation project


