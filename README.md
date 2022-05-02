# Setting Up Kind

## Install Kind Cluster
`kind create cluster --name abc`

## Install MinIO
`helm upgrade --install minio minio/minio -f minio_values.yaml -n default`

* Set the Acces key and Secret key 
* Create Some default Buckets
* Change the PVC Sizse and resources
* Port forward on 9001
* Create Airflow connection named s3_conn for Remote logging
  * Add Extra 
    `{"aws_access_key_id": "abhishek", "aws_secret_access_key": "choudhary123", "host": "http://minio:9000"}`
    Host is --endpoint_url and provide minio service http address
* 

## Setting up Airflow Remote logging


## Setting Up Apache Spark in K8s 


## Load Docker Images in Kind
```sh
kind load docker-image --name abc gcr.io/spark-operator/spark-operator:3.1.1
kind load docker-image --name abc docker.io/apache/airflow:2.2.4
kind load docker-image --name abc docker.io/apache/airflow-statsd-exporter-2021.04.28-v0.17.0
kind load docker-image --name abc docker.io/bitnami/postgresql:11.12.0-debian-10-r44
kind load docker-image --name abc gcr.io/spark-operator/spark-operator:3.1.1
kind load docker-image --name abc quay.io/minio/mc:RELEASE.2022-04-16T21-11-21Z
kind load docker-image --name abc quay.io/minio/minio:RELEASE.2022-04-26T01-20-24Z
```