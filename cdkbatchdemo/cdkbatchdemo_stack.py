from aws_cdk import (
    core,
    aws_batch as batch,
    aws_ec2 as ec2
    )


class CdkbatchdemoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        ce_resources = batch.ComputeResources(type=batch.ComputeResourceType.SPOT,
                                       bid_percentage=50,
                                       allocation_strategy=batch.AllocationStrategy.SPOT_CAPACITY_OPTIMIZED,
                                       instance_types= [ec2.InstanceType("c5.large"), ec2.InstanceType("c5.xlarge")],
                                       vpc=vpc
                                      )
                                      
        spot_environment = batch.ComputeEnvironment(self, "MySpotEnvironment",
                                                    compute_resources=ce_resources
                                                   )
        queue = batch.JobQueue(self, "BatchQueue",
                               compute_environments=[batch.JobQueueComputeEnvironment(compute_environment=spot_environment, order=1)],
                               priority=1)
        
