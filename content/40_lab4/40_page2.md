+++
title = "Modify the template"
chapter = false
weight = 42
+++


## Modify

* In VSCode, edit the `cfn_project/templates/lab3.template.yaml` file. We'll be adding the following snipplet to the _Resources_ section of the template.

```
CopyZipsTemplate:
      Type: AWS::CloudFormation::Stack
      Properties:
        TemplateURL: !Sub "https://${S3BucketName}.${AWS::Region}.amazonaws.com/${S3KeyPrefix}templates/copy-zips.template.yaml"
        Parameters:
          S3BucketName: !Ref S3BucketName
          S3KeyPrefix: !Ref S3KeyPrefix
          SourceObjects: "lambda_functions/packages/GenRandom/lambda.zip"
```

* We're also modifying the `GenRandomLambda` resource to use a template output from our `CopyZipsStack`.

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
          S3Bucket: !GetAtt 'CopyZipsTemplate.Outputs.LambdaZipsBucket'
          S3Key: !Sub '${S3KeyPrefix}lambda_functions/packages/GenRandom/lambda.zip'
```

The full template should reflect the following:

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
          Policies:
          - PolicyName: root
            PolicyDocument:
              Version: '2012-10-17'
              Statement:
              - Effect: Allow
                Action:
                - logs:*
                Resource: arn:aws:logs:*:*:*
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
      StringGenerator:
        Type: Custom::RandomString
        Properties:
          ServiceToken: !GetAtt GenRandomLambda.Arn
          Length: 12
      CopyZipsTemplate:
        Type: AWS::CloudFormation::Stack
        Properties:
          TemplateURL: !Sub "https://${S3BucketName}.${AWS::Region}.amazonaws.com/${S3KeyPrefix}templates/copy-zips.template.yaml"
          Parameters:
            S3BucketName: !Ref S3BucketName
            S3KeyPrefix: !Ref S3KeyPrefix
            SourceObjects: "lambda_functions/packages/GenRandom/lambda.zip"
Outputs:
      GeneratedRandomString:
        Description: Generated Random String
        Value: !GetAtt StringGenerator.RandomString
      LicenseToken:
        Description:  LicenseToken passed in via overrides
        Value: !Ref LicenseToken
      AvailabilityZones:
        Description:  AvailabilityZones injected via $[taskcat_genaz_3] psuedo-parameter
        Value:  !Join [ ',', !Ref 'AvailabilityZones' ]
```
