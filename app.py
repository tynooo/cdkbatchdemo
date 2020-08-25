#!/usr/bin/env python3

from aws_cdk import core

from cdkbatchdemo.cdkbatchdemo_stack import CdkbatchdemoStack


app = core.App()
CdkbatchdemoStack(app, "cdkbatchdemo")

app.synth()
