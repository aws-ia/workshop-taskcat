+++
title = "Lab 3"
chapter = false
weight = 30
+++

### Testing in multiple regions

An important part of building high-confidence CloudFormation is multi-region testing.

In this lab, we will see how **taskcat** can help uncover common issues when deploying in different regions.

We'll start off by we will use the same template which builds a Lambda backed custom resource.

To test this template we will add 2 more regions to the test definition.

- After running the test, we will see that the **us-east-1** region deploys properly, while we _receive failures in other regions._

Looking at the logs we can see that lambda source is not accessible from the other regions.

- We will then modify the our template to include a child-stack. This child stack will pre-stage the lambda source in each region.

- Finally, we'll kick off our **taskcat** test again to validate the fix we implemented!

To get started navigate to the lab3/cfn-project folder in your IDE.
