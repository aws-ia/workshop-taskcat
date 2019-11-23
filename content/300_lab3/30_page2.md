+++
title = "View test results"
chapter = false
weight = 315
+++

## Test Results

After the test completes you will see a new folder under `cfn-project` called **taskcat_outputs**
```
cfn-project
├── lambda_functions
├── templates
├── .taskcat.yml
└── taskcat_outputs/index.html < - (report)
```
To open `taskcat_outputs/index.html` in the AppStream browser, we've provided a simple 
shortcut that can be executed from the terminal:

```
open-taskcat-report
```

![fig3.2](/images/failed_outputs.png)

To see the test logs click the **View Logs** link

![fig3.2](/images/failure_logs.png)

