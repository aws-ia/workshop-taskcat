+++
title = "Modify the template"
chapter = false
weight = 320
+++


## Making our template multi-region
There are multiple potential strategies to deal with resources that require the content
in S3 to be in the same region as the stack. In this example we will add a resource to 
the stack that copies the Lambda zip from the bucket in us-east-1 to the stack region 
before creating the lambda.

* In VSCode, edit the **cfn_project/templates/lab3.template.yaml** file. We'll be adding 
the following snippet to the _Resources_ section of the template.

```yaml
    CopyZipsTemplate:
      Type: AWS::CloudFormation::Stack
      Properties:
        TemplateURL: !Sub "https://${S3BucketName}.s3.amazonaws.com/${S3KeyPrefix}templates/copy-zips.template.yaml"
        Parameters:
          S3BucketName: !Ref S3BucketName
          S3KeyPrefix: !Ref S3KeyPrefix
          SourceObjects: "lambda_functions/packages/GenRandom/lambda.zip"
```

This child stack contains a Lambda backed custom resource that takes the SourceObjects 
passed in and copies it to a new bucket in the same region as the stack. The outputs 
return the name of the new bucket, that we will use in the Code property of our 
**GenRandomLambda** resource.

```yaml
    GenRandomLambda:
      Type: AWS::Lambda::Function
      Properties:
        Description: Lambda creates simple random string
        Handler: lambda_function.handler
        Runtime: python3.7
        Role: !GetAtt 'LambdaExecutionRole.Arn'
        Timeout: 300
        Code:
          S3Bucket: !GetAtt 'CopyZipsTemplate.Outputs.LambdaZipsBucket'
          S3Key: !Sub '${S3KeyPrefix}lambda_functions/packages/GenRandom/lambda.zip'
```

The full **cfn_project/templates/lab3.template.yaml** template should reflect the 
following:

* Feel free to copy and paste!

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
      S3BucketName:
        AllowedPattern: '^[0-9a-zA-Z]+([0-9a-zA-Z-]*[0-9a-zA-Z])*$'
        ConstraintDescription: >-
          Bucket name can include numbers, lowercase letters, uppercase
          letters, and hyphens (-). It cannot start or end with a hyphen (-).
        Description: >-
          S3 bucket name for assets. Bucket name can
          include numbers, lowercase letters, uppercase letters, and hyphens (-). It
          cannot start or end with a hyphen (-).
        Type: String
      S3KeyPrefix:
        AllowedPattern: '^[0-9a-zA-Z-/]*$'
        ConstraintDescription: >-
          Can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/).
        Default: 'cfn-project/'
        Description: >-
          S3 key prefix where assets are located should end with forward slash (/).
        Type: String
Resources:
      LambdaExecutionRole:
        Type: AWS::IAM::Role
        Properties:
          AssumeRolePolicyDocument:
            Version: '2012-10-17'
            Statement:
            - Effect: Allow
              Principal:
                Service:
                - lambda.amazonaws.com
              Action:
              - sts:AssumeRole
          Path: "/"
          ManagedPolicyArns:
          - "arn:aws:iam::aws:policy/AWSLambdaExecute"
      GenRandomLambda:
        Type: AWS::Lambda::Function
        Properties:
          Description: Lambda creates simple random string
          Handler: lambda_function.handler
          Runtime: python3.7
          Role: !GetAtt 'LambdaExecutionRole.Arn'
          Timeout: 300
          Code:
            S3Bucket: !GetAtt 'CopyZipsTemplate.Outputs.LambdaZipsBucket'
            S3Key: !Sub '${S3KeyPrefix}lambda_functions/packages/GenRandom/lambda.zip'
      StringGenerator:
        Type: Custom::RandomString
        Properties:
          ServiceToken: !GetAtt GenRandomLambda.Arn
          Length: 12
      CopyZipsTemplate:
        Type: AWS::CloudFormation::Stack
        Properties:
          TemplateURL: !Sub "https://${S3BucketName}.s3.amazonaws.com/${S3KeyPrefix}templates/copy-zips.template.yaml"
          Parameters:
            S3BucketName: !Ref S3BucketName
            S3KeyPrefix: !Ref S3KeyPrefix
            SourceObjects: "lambda_functions/packages/GenRandom/lambda.zip"
Outputs:
      GeneratedRandomString:
        Description: Generated Random String
        Value: !GetAtt StringGenerator.RandomString
```
