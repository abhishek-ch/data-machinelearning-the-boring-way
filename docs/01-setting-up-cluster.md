# Prerequisites

Setting up Kind Cluster, example __abc__

## Validating kind Cluster

## Load Desired images

__Kind recommends to always load docker image and Never use Always image pull  policy__
> NOTE: The Kubernetes default pull policy is IfNotPresent unless the image tag is :latest or omitted (and implicitly :latest) in which case the default policy is Always. IfNotPresent causes the Kubelet to skip pulling an image if it already exists. If you want those images loaded into node to work as expected, please:

For Lab 1, you need the following docker image locally and then using following command to load images for kind cluster named 'abc'

```
kind load docker-image --name abc gcr.io/spark-operator/spark-operator:3.1.1

kind load docker-image --name abc docker.io/apache/airflow:2.2.4

kind load docker-image --name abc docker.io/apache/airflow-statsd-exporter-2021.04.28-v0.17.0

kind load docker-image --name abc docker.io/bitnami/postgresql:11.12.0-debian-10-r44

kind load docker-image --name abc gcr.io/spark-operator/spark-operator:3.1.1

kind load docker-image --name abc quay.io/minio/mc:RELEASE.2022-04-16T21-11-21Z

kind load docker-image --name abc quay.io/minio/minio:RELEASE.2022-04-26T01-20-24Z
```
## Verify all loaded Images

`docker exec -it abc-control-plane crictl images ps`
