# URL Shortener Helm Chart

This Helm chart deploys the URL Shortener application, including both the API and operator components.

## Prerequisites

- Kubernetes 1.19+
- Helm 3.2.0+
- Ingress controller (like nginx-ingress) installed in your cluster

## Installing the Chart

To install the chart with the release name `my-release`:

```bash
helm install my-release ./url-shortener-chart
```

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```bash
helm uninstall my-release
```

## Parameters

### Global Parameters

| Name | Description | Default |
|------|-------------|---------|
| `nameOverride` | String to partially override the fullname template | `""` |
| `fullnameOverride` | String to fully override the fullname template | `""` |

### API Parameters

| Name | Description | Default |
|------|-------------|---------|
| `api.image.repository` | API image repository | `dibaro/shorturl-api` |
| `api.image.tag` | API image tag | `latest` |
| `api.image.pullPolicy` | API image pull policy | `Always` |
| `api.replicas` | Number of API replicas | `1` |
| `api.service.type` | API service type | `ClusterIP` |
| `api.service.port` | API service port | `80` |
| `api.service.targetPort` | API container port | `5000` |
| `api.resources.limits.cpu` | API CPU limits | `200m` |
| `api.resources.limits.memory` | API memory limits | `256Mi` |
| `api.resources.requests.cpu` | API CPU requests | `100m` |
| `api.resources.requests.memory` | API memory requests | `128Mi` |
| `api.ingress.enabled` | Enable ingress for API | `true` |
| `api.ingress.className` | Ingress class name | `nginx` |
| `api.ingress.hosts` | Ingress hosts configuration | See values.yaml |

### Operator Parameters

| Name | Description | Default |
|------|-------------|---------|
| `operator.image.repository` | Operator image repository | `dibaro/shorturl-operator` |
| `operator.image.tag` | Operator image tag | `latest` |
| `operator.image.pullPolicy` | Operator image pull policy | `Always` |
| `operator.replicas` | Number of operator replicas | `1` |
| `operator.resources.limits.cpu` | Operator CPU limits | `200m` |
| `operator.resources.limits.memory` | Operator memory limits | `256Mi` |
| `operator.resources.requests.cpu` | Operator CPU requests | `100m` |
| `operator.resources.requests.memory` | Operator memory requests | `128Mi` | 