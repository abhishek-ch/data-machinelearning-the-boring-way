# Data & Machine Learning - The Boring Way

This tutorial walks you through setting up and building a Data Engineering & Machine Learning Plaform. 
The tutorial is designed to explore many different technologies for similar problem without any bias. This will help developers
to pick a particular technology

__This is not a Production Ready Setup and its as well not the best way__


## Target Audience
Data Engineers, Machine Learning Engineer, Data Scientist, SRE, Infrastructure Engineer, Data Analysts, Data Analytics Engineer

# Expected Technologies & Workflow 

## Data Engineering & Analytics
- [ ] Kubernetes Kind Installation
- [ ] [Apache Airflow](https://airflow.apache.org/) on top of Kubernetes & Running an end to end Airflow Workflow using Kubernetes Executor
- [ ] [Apache Spark](https://spark.apache.org/) Deploy Apache Spark on Kubernetes and run workflow 
- [ ] [Prefect](https://www.prefect.io/) Setup & Running an end to end Workflow
- [ ] [Dagster](https://dagster.io/) Setup & Running an end to end Workflow
- [ ] [Mino](https://min.io/) Integrate Object Storage on top of Kubernetes and use minio interface for simulating the s3
- [ ] [Apache Hive](https://cwiki.apache.org/confluence/display/hive/design) Setting up Hive & Hive Metastore
- [ ] Deploy Trino & Open Source [Presto](https://prestodb.io/) and run dana Analytics queries.
- [ ] Integrate [Superset](https://superset.apache.org/) & [Metabase](https://www.metabase.com/) to run visualization. Integrate Presto with the visualization system.
- [ ] Open Table Format using [Delta](https://docs.delta.io/latest/quick-start.html)
- [ ] Open Table Format using [Apache Iceberg](https://iceberg.apache.org/)
- [ ] Open Table Format using [Apache Hudi](https://hudi.apache.org/)
- [ ] Metadata Management using [Amundsen](https://www.amundsen.io/)
- [ ] Metadata Management using [Datahub](https://datahubproject.io/)
- [ ] Setting up [Apache Kafka](https://kafka.apache.org/) distributed event streaming platform
- [ ] Using Spark Structered Streaming to run an end-2-end pipeline over any realtime data sources
- [ ] Using [Apache Flink](https://flink.apache.org/) to run an end-2-end pipeline over any realtime data sources
- [ ] [Redpanda](https://redpanda.com/), streaming data platform to run similar workflow
- [ ] [Airbyte](https://airbyte.com/) Data Integration platform
- [ ] [Talend](https://www.talend.com/products/data-integration/) UI based Data Integration
- [ ] [DBT](https://www.getdbt.com/) DBT Sql Pipeline to compare with Spark and other tech
- [ ] [Debezium](https://debezium.io/) Change Data Capture using Debezium to sync multiple databases

## Monitoring & Observability

## Machine Learning

## Prerequisites
* 🐳 Docker Installed 
* [kubectl](https://kubernetes.io/docs/tasks/tools/) Installed, The Kubernetes command-line tool, kubectl, allows you to run commands against Kubernetes clusters
* [Lens](https://k8slens.dev/) Installed, UI for Kubernetes.  
_This is optional, kubectl is enough for getting all relevant stats from kubernetes cluster_
* [Helm](https://helm.sh/) The package manager for Kubernetes

## Lab Basic Setup
* [Setting Up Kind](https://kind.sigs.k8s.io/docs/user/quick-start/)

## Install & Set Kind Cluster
```
$ kind create cluster --name abc

$ kubectl config use-context kind-abc
```

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