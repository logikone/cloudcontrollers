from enum import Enum


class HTTPMethod(Enum):
    GET = 0
    POST = 1
    PUT = 2
    PATCH = 3
    DELETE = 4


class ApiGroup(Enum):
    AWS = 'aws.cloudcontrollers.io'


class ApiVersion(Enum):
    V1Alpha1 = 'v1alpha1'
