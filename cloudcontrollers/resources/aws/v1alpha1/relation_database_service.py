from kubernetes.client import V1ObjectMeta, V1beta1CustomResourceDefinitionNames

from cloudcontrollers.resources import CustomResourceDefinition, CustomResourceDefinitionSpec
from cloudcontrollers.resources.aws import API_GROUP
from cloudcontrollers.resources.aws.v1alpha1 import API_VERSION


class RelationalDatabaseServiceResource(CustomResourceDefinition):
    singular_name = 'relationaldatabase'
    plural_name = f'{singular_name}s'

    def __init__(self):
        super().__init__(
            metadata=V1ObjectMeta(
                name=f'{self.plural_name}.{API_GROUP}'
            ),
            spec=CustomResourceDefinitionSpec(
                group=API_GROUP,
                version=API_VERSION,
                scope='Namespaced',
                names=V1beta1CustomResourceDefinitionNames(
                    plural=self.plural_name,
                    singular=self.singular_name,
                    kind='RelationalDatabase',
                    short_names=['rds']
                )
            ),
        )
