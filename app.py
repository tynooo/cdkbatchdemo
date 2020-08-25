#!/usr/bin/env python3
import os
from aws_cdk import core

from cdkbatchdemo.infra_stack import InfraStack
from cdkbatchdemo.cdkbatchdemo_stack import CdkbatchdemoStack


app = core.App()


ACCOUNT = app.node.try_get_context('account') or os.environ.get(
    'CDK_DEFAULT_ACCOUNT', 'unknown')
REGION = app.node.try_get_context('region') or os.environ.get(
    'CDK_DEFAULT_REGION', 'unknown')
AWS_ENV = core.Environment(region=REGION, account=ACCOUNT)


infra_stack = InfraStack(app, "BatchDemoInfra", env=AWS_ENV)
batch_stack = CdkbatchdemoStack(app, "cdkbatchdemo",
                                env=AWS_ENV,
                                vpc=infra_stack.vpc
                               )

app.synth()
