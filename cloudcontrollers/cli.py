import asyncio
import signal

import click
import uvloop

from cloudcontrollers import CloudControllers
from cloudcontrollers.logging import logger


@click.command()
def cli():
    asyncio.set_event_loop_policy(
        uvloop.EventLoopPolicy()
    )

    loop = asyncio.get_event_loop()
    _add_signal_handlers(loop)

    loop.create_task(
        CloudControllers(loop).run()
    )

    loop.run_forever()


def _add_signal_handlers(loop: asyncio.AbstractEventLoop):
    def handle_sigint():
        logger.info("Caught SIGINT. Stopping ...")
        loop.stop()

    loop.add_signal_handler(signal.SIGINT, handle_sigint)
