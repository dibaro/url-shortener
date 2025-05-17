from flask import Flask, redirect, abort
from kubernetes import client, config
import os

app = Flask(__name__)

config.load_incluster_config()
co_api = client.CustomObjectsApi()

GROUP = "urlshortener.tapsi.ir"    
VERSION = "v1"                    
PLURAL = "shorturls"             
# NAMESPACE = os.environ.get("NAMESPACE", "default")  

@app.route('/<string:short_path>')
def redirect_shorturl(short_path):
    try:
        # shorturls = co_api.list_namespaced_custom_object(
        #     group=GROUP,
        #     version=VERSION, 
        #     namespace=NAMESPACE
        #     plural=PLURAL
        # )
        shorturls = co_api.list_cluster_custom_object(
            group=GROUP,
            version=VERSION,
            plural=PLURAL
        )
    except Exception as e:
        return f"Error accessing Kubernetes API: {e}", 500

    for item in shorturls.get('items', []):
        status = item.get('status', {})
        if status.get('shortPath') == '/'+short_path:
            name = item['metadata']['name']
            target_url = item['spec'].get('targetURL')
            new_count = status.get('clickCount', 0) + 1

            body = {'status': {'clickCount': new_count}}
            namespace = item['metadata']['namespace']
            co_api.patch_namespaced_custom_object_status(
                group=GROUP,
                version=VERSION,
                namespace=namespace,
                plural=PLURAL,
                name=name, body=body
            )

            return redirect(target_url, code=302)

    return abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
