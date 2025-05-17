import kopf
import kubernetes
import random
import string

try:
    kubernetes.config.load_incluster_config()
except:
    kubernetes.config.load_kube_config()
api = kubernetes.client.CustomObjectsApi()

@kopf.on.create('urlshortener.tapsi.ir', 'v1', 'shorturls')
def create_shorturl(spec, name, namespace, logger, **kwargs):
    target = spec.get('targetURL')
    logger.info(f"Creating ShortURL for target: {target}")

    short_key = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
    short_path = f"/{short_key}"
    initial_count = 0

    status = {"shortPath": short_path, "clickCount": initial_count}
    api.patch_namespaced_custom_object_status(
        group="urlshortener.tapsi.ir", version="v1",
        namespace=namespace, plural="shorturls", name=name,
        body={"status": status}
    )
    logger.info(f"Set shortPath={short_path}, clickCount={initial_count} in status")

