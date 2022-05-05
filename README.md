# Data & Machine Learning - The Boring Way

This tutorial walks you through setting up and building a Data Engineering & Machine Learning Platform. 
The tutorial is designed to explore many different technologies for the similar problems without any bias. 

__This is not a Production Ready Setup__

## Target Audience
Data Engineers, Machine Learning Engineer, Data Scientist, SRE, Infrastructure Engineer, Data Analysts, Data Analytics Engineer

# Expected Technologies & Workflow 

## Data Engineering & Analytics
- [X] Kubernetes Kind Installation [link](/docs/01-setting-up-cluster.md)
- [X] [Apache Airflow](https://airflow.apache.org/) on top of Kubernetes & Running an end to end Airflow Workflow using Kubernetes Executor
- [X] [Apache Spark](https://spark.apache.org/) Deploy Apache Spark on Kubernetes and run an example [link](/docs/02-setting-up-apachespark-k8s.md)
- [ ] [Prefect](https://www.prefect.io/) Setup & Running an end to end Workflow
- [ ] [Dagster](https://dagster.io/) Setup & Running an end to end Workflow
- [X] [Mino](https://min.io/) Integrate Object Storage on top of Kubernetes and use minio interface for simulating the s3
- [ ] Set up an ETL job running end-2-end on apache airflow. This job contains Spark & Python Operator
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
- [ ] [Grafana]([https://](https://grafana.com/)) Setting Up Grafana for Monitoring components. Start with Monitoring Pods
- [ ] [FluentD](https://www.fluentd.org/) logging metrics from pods & interact the same with Monitoring layer
- [ ] Setting up a full Monitoring and Alerting Platform & integrate minitoring across other technologies
- [ ] Setting up an Observability system 

## Machine Learning
- [ ] Setup [Ray](https://www.ray.io/) for Data Transformations
- [ ] Use [Scikit-learn](https://scikit-learn.org/) for an example ML training
- [ ] Setup [Argo Pipeline](https://argoproj.github.io/) for deploying ML Jobs
- [ ] Setup [Flyte](https://flyte.org/) Orchestrator for pythonic Deployment
- [ ] Use [Pytorch Lightening](https://www.pytorchlightning.ai/) for runing ML training
- [ ] Use Tensorflow for running ML training
- [ ] Setup ML End-2-End Workflow on Flyte
- [ ] Deploy [MLFlow](https://www.mlflow.org/docs/latest/index.html) for ML Model Tracking & Experimentation
- [ ] Deploy [BentoML](https://www.bentoml.com/) For deploying ML Model
- [ ] Deploy [Sendon Core](https://github.com/SeldonIO/seldon-core) for ML Model Management
- [ ] Integrate MLflow with Seldon Core 

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