import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="transaction_processor",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "transaction_processor"},
    packages=setuptools.find_packages(where="transaction_processor"),

    install_requires=[
        "aws-cdk.core==1.77.0",
        "aws-cdk.aws-lambda==1.77.0",
        "aws-cdk.aws-sns==1.77.0",
        "aws-cdk.aws-sns-subscriptions==1.77.0",
        "aws-cdk.aws-stepfunctions==1.77.0",
        "aws-cdk.aws_stepfunctions_tasks==1.77.0",
        "aws-cdk.aws-secretsmanager==1.77.0",
        "aws-cdk.aws-events==1.77.0",
        "aws-cdk.aws-events-targets==1.77.0",
        "aws-cdk.aws-secretsmanager==1.77.0",
        "aws-cdk.aws-s3==1.77.0",
        "cdk_watchful==0.5.45",
        "boto3==1.16.23 "
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
