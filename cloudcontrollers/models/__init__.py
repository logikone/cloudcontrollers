from kubernetes.client import V1ObjectMeta


class CloudControllersResourceSpec(object):
    def to_dict(self):
        raise NotImplementedError


class CloudControllersResourceStatus(object):
    def to_dict(self):
        raise NotImplementedError


class CloudControllersResource(object):
    attribute_map = {
        'api_version': 'apiVersion',
        'kind':        'kind',
        'metadata':    'metadata',
        'spec':        'spec',
        'status':      'status',
    }

    def __init__(self,
                 api_version: str = None,
                 kind: str = None,
                 metadata: V1ObjectMeta = None,
                 spec: CloudControllersResourceSpec = None,
                 status: CloudControllersResourceStatus = None):
        self.api_version = api_version
        self.kind = kind
        self.metadata = metadata
        self.spec = spec
        self.status = status

    def __repr__(self):
        return f"<{self.__class__.__name__}: " \
               f"apiVersion={self.api_version}," \
               f"kind={self.kind}," \
               f"metadata={self.metadata}," \
               f"spec={self.spec}," \
               f"status={self.status}>"

    def to_dict(self):
        return dict(
            api_version=self.api_version,
            kind=self.kind,
            metadata=self.metadata.to_dict(),
            spec=self.spec.to_dict(),
            status=self.status.to_dict(),
        )


class CloudControllersResourceList(object):
    attribute_map = {
        'api_version': 'apiVersion',
        'items':       'items',
        'kind':        'kind',
        'metadata':    'metadata',
    }

    def __init__(self,
                 api_version: str = None,
                 items: list = None,
                 kind: str = None,
                 metadata: V1ObjectMeta = None):
        if items is None:
            items = list()

        self.api_version = api_version
        self.items = items
        self.kind = kind
        self.metadata = metadata

    def __iter__(self):
        for item in self.items:
            yield item

    def to_dict(self):
        return dict(
            apiVersion=self.api_version,
            # items=map(lambda x: x.to_dict(), self.items),
            items=self.items,
            kind=self.kind,
            metadata=self.metadata.to_dict()
        )
