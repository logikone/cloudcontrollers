import sys
from asyncio import AbstractEventLoop, sleep

from cloudcontrollers.controllers import KubernetesController
from cloudcontrollers.logging import banner, logger
from cloudcontrollers.resources import CustomResourceDefinition


class CloudControllers(object):
    def __init__(self, loop: AbstractEventLoop):
        self.loop = loop

    async def run(self):
        self._print_banner()

        logger.info("Starting CloudControllers Service")
        await self._register_custom_resources()
        self._start_watchers()

    @staticmethod
    async def _register_custom_resources():
        logger.info("Registering Custom Resource Definitions")

        for crd in CustomResourceDefinition.__subclasses__():
            await crd().register()

    def _start_watchers(self):
        logger.info("Starting Custom Resource Watchers")

        for controller in KubernetesController.__subclasses__():
            self.loop.create_task(controller().run())
            sleep(1)

    @staticmethod
    def _print_banner():
        sys.stdout.write(f'{banner}\n\n')
