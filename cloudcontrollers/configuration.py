from kubernetes import config

try:
    config.load_incluster_config()
except config.ConfigException:
    config.load_kube_config()
