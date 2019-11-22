+++
title = "Lambda packaging"
chapter = false
+++



## Test staging

From your vscode terminal change directory to your project root for **lab1** __(lab1/cfn-project)__

Under cfn-project you will see the following files
```
cfn-project
├── lambda_functions/source/GenRandom/
├── templates/lab1.template.yaml
└── .taskcat.yml
```

The provided template for lab1 uses lambda backed custom resource.

**source/GenRandom** contains the lambda source. 

When lambda source is detected taskcat will package the lambda zip file and then save it 
to lambda_functions/packages/. This zip file is referenced in our lambda function.

> Note: The default source and package folders can be changed by setting values in your 
> project_config file.

> Note: taskcat is able to build dependencies for your lambda so that you don't need to 
> check them into source control. This can be done by providing a Dockerfile  that 
> contains the in the build steps in source folder. Or, for python functions, if a 
> requirements.txt file is found, taskcat will package the dependencies defined in it 
> into your zip.

```
  GenRandomLambda:
    Type: AWS::Lambda::Function
    Properties:
      Description: Lambda creates simple random string
      Handler: lambda_function.handler
      Runtime: python3.7
      Role: !GetAtt 'LambdaExecutionRole.Arn'
      Timeout: 300
      Code:
        S3Bucket: !Ref 'S3BucketName'
        S3Key: !Sub '${S3KeyPrefix}lambda_functions/packages/GenRandom/lambda.zip'
```

If you want to run packaging step on its own you can run `taskcat package`

This is _optional_, In the next step we will execute the taskcat test which will run 
packaging prior to test execution.




