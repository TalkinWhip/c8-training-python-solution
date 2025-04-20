import asyncio
import logging
from pyzeebe import ZeebeClient, ZeebeWorker, ZeebeTaskRouter, create_camunda_cloud_channel, Job

# Setup logging
# logging.basicConfig(level=logging.Debug)

# Define tasks
router = ZeebeTaskRouter()

@router.task("example-job")
def deduct_credit(job: Job):
    print(f"Hello world")
    return

# Create a channel, the worker and include the router with tasks
async def main():
    grpc_channel = create_camunda_cloud_channel(client_id="xxx",
                                                client_secret="xxx",
                                                cluster_id="xxx",
                                                region="bru-2")
    worker = ZeebeWorker(grpc_channel)
    worker.include_router(router)
    await worker.work()

asyncio.run(main())
