import time
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import datetime
from airflow.configuration import conf
from airflow.operators.bash import BashOperator
from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import SparkKubernetesOperator
from airflow.providers.cncf.kubernetes.sensors.spark_kubernetes import SparkKubernetesSensor
from airflow.operators.python import BranchPythonOperator

default_args = {
    'owner': 'abc',
    'team': 'dataengineering',
    'depends_on_past': False,
    'start_date': datetime.utcnow(),
    'email': ['somebody@foo.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'max_active_runs': 1,
}

with DAG(
        'Basic_Transformation',
        default_args=default_args,
        description='Basics Transformation to work with CSV & parquet using PySpark',
        schedule_interval=None,
        concurrency=10,
        tags=['basic', 'pyspark'],
) as dag:

    start = DummyOperator(task_id='start', dag=dag, trigger_rule='all_success')

    def print_variables(**context):
        SOURCE = context["dag_run"].conf["source_path"]
        DESTINATION = context["dag_run"].conf["destination_path"]

        print('Source Path {0}'.format(SOURCE))
        print('Destination Path {0}'.format(DESTINATION))

    print_variable = PythonOperator(
        task_id='print_the_context',
        python_callable=print_variables,
    )

    csv_to_parquet = SparkKubernetesOperator(
        task_id="csv_to_parquet",
        namespace="default",
        application_file="runners/csvtopqt.yaml",
        do_xcom_push=True
    )

    csv_to_parquet_sensor = SparkKubernetesSensor(
        task_id="csv_to_parquet_sensor",
        namespace="default",
        attach_log=True,
        application_name="{{ ti.xcom_pull(task_ids='csv_to_parquet')['metadata']['name'] }}",
        kubernetes_conn_id="kubernetes_default"
    )

    process_data = SparkKubernetesOperator(
        task_id="process_data",
        namespace="default",
        application_file="runners/accountbypartition.yaml",
        do_xcom_push=True
    )

    process_data_sensor = SparkKubernetesSensor(
        task_id="process_data_sensor",
        namespace="default",
        attach_log=True,
        application_name="{{ ti.xcom_pull(task_ids='process_data')['metadata']['name'] }}",
        kubernetes_conn_id="kubernetes_default"
    )

    end = DummyOperator(task_id='end', dag=dag, trigger_rule='all_success')
    
    start >> print_variable >> csv_to_parquet >> csv_to_parquet_sensor
    csv_to_parquet_sensor >> process_data >> process_data_sensor >> end