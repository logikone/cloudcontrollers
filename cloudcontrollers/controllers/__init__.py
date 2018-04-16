from pprint import pprint

from cloudcontrollers.apis import CloudControllersResourceApi


class KubernetesController(object):
    def __init__(self, api: CloudControllersResourceApi):
        self.api = api

    def __repr__(self):
        return f'<{self.__class__.__name__}>'

    async def run(self):
        resources = await self.api.list_resources(True)

        pprint(resources.to_dict())
