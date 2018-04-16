import asyncio
import json

from kubernetes.client import (
    ApiextensionsV1beta1Api,
    V1ObjectMeta,
    V1beta1CustomResourceDefinition,
    V1beta1CustomResourceDefinitionSpec,
    V1beta1CustomResourceDefinitionStatus,
)
from kubernetes.client.rest import ApiException

from cloudcontrollers.logging import logger

API_GROUP = u'cloudcontrollers.io'


class CustomResourceDefinitionSpec(V1beta1CustomResourceDefinitionSpec):
    def __init__(self,
                 group=API_GROUP,
                 names=None,
                 scope=None,
                 subresources=None,
                 validation=None,
                 version=None):
        super().__init__(group=group,
                         names=names,
                         scope=scope,
                         subresources=subresources,
                         validation=validation,
                         version=version)


class CustomResourceDefinition(V1beta1CustomResourceDefinition):
    def __init__(self,
                 metadata: V1ObjectMeta,
                 spec: CustomResourceDefinitionSpec,
                 status: V1beta1CustomResourceDefinitionStatus = None):
        super().__init__(
            api_version=u'apiextensions.k8s.io/v1beta1',
            kind=None,
            metadata=metadata,
            spec=spec,
            status=status,
        )

        self.api = ApiextensionsV1beta1Api()
        self.loop = asyncio.get_event_loop()

    async def register(self):
        logger.debug(f'Registering CRD: {self.metadata.name}')

        try:
            await self.loop.run_in_executor(None,
                                            self.api.create_custom_resource_definition,
                                            self)
        except ApiException as creation_error:
            if creation_error.status != 409:
                error = json.loads(creation_error.body)['message']
                logger.error(f'Error creating Custom Resource Definition. Reason: {error}')
        except ValueError as value_error:
            logger.error(f'Error creating Custom Resource Definition. Reason: {value_error}')
