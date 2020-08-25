from aws_cdk import (
    core,
    aws_ec2 as ec2,
    )


class InfraStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #Build new VPC
        self.vpc = ec2.Vpc(
            self, "DemoVPC",
            cidr=self.node.try_get_context("vpc_cidr"),
            subnet_configuration=[
                # Only using public for this demo so that we don't create NAT GWs
                {"cidrMask": 24, "name": "ecsvpc", "subnetType": ec2.SubnetType.PUBLIC},
                # {"cidrMask": 24, "name": "ecsprivatevpc", "subnetType": ec2.SubnetType.PRIVATE}
            ]
        )
