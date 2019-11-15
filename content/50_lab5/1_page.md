+++
title = "Initialize Git repo"
chapter = false
weight = 51
+++

To create a CICD pipeline for your project, you need a git repository. This repository will contain all the source code of your project and will be the source to trigger your pipeline.

For this lab, you will use AWS CodeCommit for your project's git repository. We have already pre-created a Code Commit repsoitory in your team's AWS Account. Click the following link to open the AWS CodeCommit console in a new tab of your browser.

[**AWS CodeCommit repo**](https://us-west-2.console.aws.amazon.com/codesuite/codecommit/repositories/quiz-app/browse?region=us-west-2)

### Initialize Git

Now, you need to push your source code into your AWS CodeCommit repository. You will create 2 branches in your repository - **master** and **develop**. 

**master** branch is the release branch of your project. You will not make any changes to the master branch directly. 

**develop** branch is your development branch. Any changes you are making in your code, you will do it in the develop branch. When you push your changes to the remote develop branch, pipeline will get triggered, which will test your changes and if the tests are successfully finished, develop branch will be merged into the master branch.

Follow the below steps to push your changes from your development environment to the AWS CodeCommit repository, in your AWS account.

1. Goto your development environment and in the terminal window, run the following command to make sure you are in the **lab5/cfn-project** folder - ``cd /mnt/c/Users/Public/Documents/Workshop/workshop/content/lab_assets/start/lab5/cfn-project/``.

2. Run `git init`, to initialize the git repository in your project folder. This will automatically create and checkout the **master** branch.

3. Replace **YOUR-NAME** with your name, in `git config user.name "YOUR-NAME"` and run it to configure your git username.

4. Run `git commit --allow-empty -m "root commit"`, to make an empty commit to the master branch. Git doesn't allow to push empty branches to the remote repository. Therefore you are creating an empty commit by running this command.

5. Run `git checkout -b develop`, to make the **develop** branch as your working directory.

6. Run `git add .`, to stage all your changes.

7. Run `git commit -m "Initial code"`, to commit your changes locally.

8. Go to your team's dashboard and copy **CodeCommit git URL**. Replace **CODE-COMMIT-REPO-URL** with the URL you copied in the following command and run it. `git remote add origin CODE-COMMIT-REPO-URL`.

9. Run `git push origin --all`, to push your changes to the remote repository. When prompted, enter the AWS CodeCommit git username and password, which you can get from your team's dashboard.

Go to your AWS CodeCommit repository and you should see the source code in the **develop** branch. **master** branch will be empty.