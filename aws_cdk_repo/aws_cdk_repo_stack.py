from aws_cdk import( 
    aws_s3 as s3,
    core as cdk,
    aws_lambda as _lambda
    )

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.



class AwsCdkRepoStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(self, "cdkbucket", bucket_name= "cdk-bucket-aj1505", public_read_access=True)
        cdk.CfnOutput(self, "cdkbucket-1", value= bucket.bucket_name)

        func = _lambda.Function(
        self, 'HelloHandler',
        runtime=_lambda.Runtime.PYTHON_3_7,
        code=_lambda.Code.asset('lambda'),
        handler='hello.handler',
        )