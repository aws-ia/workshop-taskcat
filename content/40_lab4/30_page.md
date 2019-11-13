+++
title = "Code push, test and promote"
chapter = false
weight = 30
+++

### Push changes to remote repository

After you have commited your changes locally, it's time to push it to the remote repository.
Run `git push` to push your changes.

### Test execution and code promotion

Now, go to your AWS Code Pipeline console, click your pipeline, and you should see the **Source** action in-progress. After the **Source** action is completed successfully, **Build** action will start.

[TODO:Screenshot]

**Build** action uses AWS CodeBuild to run tests (as defined in your project configuration file) using TaskCat. After all the tests are completed successfully, the source branch (where the changes were commited) is merged into the release/target branch.

[TODO:Screenshot]