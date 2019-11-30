+++
title = "Clean up tests"
chapter = false
weight = 410
+++


## List tests 

* taskcat can list the tests that have not been cleaned up yet

```
taskcat test list
```

The output will display the test name, id and region for each active stack launched by 
taskcat

### Delete the test

Using the id from the list command, clean up the test:

```
taskcat test clean <TEST_ID>
```

{{% notice tip %}}
You can clean up all tests in your account with `taskcat test clean ALL`
{{% /notice %}}
