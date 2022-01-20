#!/usr/bin/python3

import boto3

ec2=boto3.resource("ec2")
instance=ec2.create_instances(
        ImageID="ami-324k548",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro")
print(instance[0].id)
