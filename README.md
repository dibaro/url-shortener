# URL Shortener Application

A Kubernetes-native URL shortener service using custom resources and an operator pattern.

## Architecture

This application consists of several components:

1. **Custom Resource Definition (CRD)**: Defines the `ShortURL` resource type
2. **Operator**: Manages `ShortURL` custom resources
3. **API Service**: Provides HTTP endpoints for creating and accessing shortened URLs

### Component Overview

#### ShortURL CRD

The `ShortURL` custom resource allows you to define URLs to be shortened:

```yaml
apiVersion: urlshortener.tapsi.ir/v1
kind: ShortURL
metadata:
  name: example-url
spec:
  targetURL: "https://example.com/very/long/path/to/shorten"
```

The operator will process this resource and update its status with the shortened path and click tracking:

```yaml
status:
  shortPath: "abc123"
  clickCount: 42
```

#### Operator

The URL shortener operator:

- Watches for `ShortURL` resources
- Generates short codes
- Maintains the mapping between short codes and target URLs
- Updates resource status with metrics

#### API Service

The API service provides:

- Endpoints for creating new shortened URLs
- Redirection from short URLs to their targets
- Click tracking and metrics

## Prerequisites

- Kubernetes 1.19+
- Helm 3.2.0+
- Ingress controller (such as nginx-ingress)
- Container registry access for the application images

## Installation

### Using Helmfile

1. **Clone the repository**:

   ```bash
   git clone https://github.com/dibaro/url-shortener.git
   cd url-shortener/releases/url-shortener
   ```

2. **Install using helmfile**:

   ```bash
   helmfile apply
   ```

   This will install all components defined in the helmfile.yaml.
