from cloudcontrollers.apis.aws.relational_database_service import RelationalDatabaseServiceApi
from cloudcontrollers.controllers import KubernetesController
from cloudcontrollers.core.constants import ApiVersion


class RelationDatabaseServiceController(KubernetesController):
    def __init__(self):
        super().__init__(RelationalDatabaseServiceApi(ApiVersion.V1Alpha1))
