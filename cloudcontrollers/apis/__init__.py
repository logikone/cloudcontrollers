import asyncio
import functools
from typing import Type

from kubernetes.client import ApiClient

from cloudcontrollers.core.constants import ApiGroup, ApiVersion, HTTPMethod
from cloudcontrollers.logging import logger
from cloudcontrollers.models import CloudControllersResource, CloudControllersResourceList


class CloudControllersResourceApi(object):
    def __init__(self,
                 api_group: ApiGroup,
                 api_version: ApiVersion,
                 list_resource_type: Type[CloudControllersResourceList],
                 resource_type: Type[CloudControllersResource]):
        self.api_client = ApiClient()
        self.api_group = api_group.value
        self.api_version = api_version.value
        self.list_resource_type = list_resource_type
        self.resource_type = resource_type

        self.loop = asyncio.get_event_loop()

    @property
    def resource_path(self):
        return f'/apis/{self.api_group}/{self.api_version}'

    async def create_resource(self, resource: CloudControllersResource):
        return await self.build_request(
            method=HTTPMethod.POST,
            body=resource
        )

    async def delete_resource(self, resource: CloudControllersResource):
        return await self.build_request(
            resource_path=f'{self.resource_path}/{resource.metadata.name}',
            method=HTTPMethod.DELETE,
            body=resource
        )

    async def get_resource(self, resource: CloudControllersResource):
        return await self.build_request(
            resource_path=f'{self.resource_path}/{resource.metadata.name}',
            method=HTTPMethod.GET,
            body=resource
        )

    async def list_resources(self, watch: bool = False):
        result, status, headers = await self.build_request(
            method=HTTPMethod.GET,
            resource_path=f'{self.resource_path}/relationaldatabases',
            path_params=dict(
                watch=watch
            ),
            response_type=self.list_resource_type
        )

        return result

    async def patch_resource(self, resource: CloudControllersResource):
        return await self.build_request(
            resource_path=f'{self.resource_path}/{resource}',
            method=HTTPMethod.PATCH,
            body=resource
        )

    async def replace_resource(self, resource: CloudControllersResource):
        return await self.build_request(
            resource_path=f'{self.resource_path}/{resource.metadata.name}',
            method=HTTPMethod.PUT,
            body=resource
        )

    def build_request(self,
                      resource_path: str = None,
                      method: HTTPMethod = None,
                      path_params=None,
                      query_params=None,
                      header_params=None,
                      body: CloudControllersResource = None,
                      post_params=None,
                      response_type=None):
        if response_type is None:
            response_type = self.resource_type

        if resource_path is None:
            resource_path = self.resource_path

        if method is None:
            method = HTTPMethod.GET

        if body is not None:
            body = body.to_dict()

        partial = functools.partial(self.api_client.call_api,
                                    resource_path=resource_path,
                                    method=method.name,
                                    path_params=path_params,
                                    query_params=query_params,
                                    header_params=header_params,
                                    body=body,
                                    post_params=post_params,
                                    response_type=response_type
                                    )

        logger.debug(f"Making request: {partial.keywords}")

        return self.loop.run_in_executor(None, partial)
