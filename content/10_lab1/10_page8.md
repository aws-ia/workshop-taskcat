+++
title = "Lambda packaging"
chapter = false
weight = 17
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

When lambda source is detected taskcat will spin up a docker container and build the lambda zip file and then save it to lambda_functions/packages/ This zip file is referenced in our lambda function

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

This is _optional_, In the next step we will execute the taskcat test which will run packaging prior to test execution




