from typing import List

from kubernetes.client import V1ObjectMeta

from cloudcontrollers.models import (
    CloudControllersResource,
    CloudControllersResourceList,
    CloudControllersResourceSpec,
    CloudControllersResourceStatus,
)


class RelationalDatabaseServiceSpec(CloudControllersResourceSpec):
    def __init__(self,
                 masterUsername: str,
                 masterUserPassword: str):
        self.master_username = masterUsername
        self.master_password = masterUserPassword

    def to_dict(self):
        return dict(
            masterUsername=self.master_username,
            masterUserPassword=self.master_password,
        )


class RelationalDatabaseServiceStatus(CloudControllersResourceStatus):
    def __init__(self, availableReplicas: int):
        self.available_replicas = availableReplicas

    def to_dict(self):
        return dict(
            availableReplicas=self.available_replicas
        )


class RelationalDatabaseService(CloudControllersResource):
    swagger_types = {
        'api_version': 'str',
        'kind':        'str',
        'metadata':    'V1ObjectMeta',
        'spec':        RelationalDatabaseServiceSpec,
        'status':      RelationalDatabaseServiceStatus,
    }

    def __init__(self,
                 api_version: str = None,
                 kind: str = None,
                 metadata: V1ObjectMeta = None,
                 spec: RelationalDatabaseServiceSpec = None,
                 status: RelationalDatabaseServiceStatus = None):
        super().__init__(api_version,
                         kind,
                         metadata,
                         spec,
                         status)


class RelationalDatabaseServiceList(CloudControllersResourceList):
    swagger_types = {
        'api_version': 'str',
        'kind':        'str',
        'items':       [RelationalDatabaseService],
        'metadata':    'V1ObjectMeta',
    }

    def __init__(self,
                 api_version: str = None,
                 items: List[RelationalDatabaseService] = None,
                 kind: str = None,
                 metadata: V1ObjectMeta = None):
        super().__init__(
            api_version=api_version,
            items=items,
            kind=kind,
            metadata=metadata
        )
