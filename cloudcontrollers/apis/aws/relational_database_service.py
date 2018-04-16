from cloudcontrollers.apis import CloudControllersResourceApi
from cloudcontrollers.core.constants import ApiGroup, ApiVersion

from cloudcontrollers.models.aws.relational_database_service import (
    RelationalDatabaseService,
    RelationalDatabaseServiceList,
)


class RelationalDatabaseServiceApi(CloudControllersResourceApi):
    def __init__(self, api_version: ApiVersion):
        super().__init__(
            api_group=ApiGroup.AWS,
            api_version=api_version,
            list_resource_type=RelationalDatabaseServiceList,
            resource_type=RelationalDatabaseService)
