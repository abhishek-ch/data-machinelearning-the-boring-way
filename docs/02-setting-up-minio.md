# MinIO

MinIO offers high-performance, S3 compatible object storage.
Minio is an object storage server that implements the same public API as Amazon S3. This means that applications that can be configured to talk to Amazon S3 can also be configured to talk to Minio

https://github.com/minio/minio

## Install MinIO
`helm upgrade --install minio minio/minio -f minio_values.yaml -n default`

* Set the `accessKey` and `secretKey` inside users key. This key is the exact representation of AWS_KEY & AWS_SECRET with Admin Buckets
* Creating 2 default buckets for Airflow log and normal data processing as `airflow-logs` & `test-files`
* Change the PVC Size and resources based on the available resources.
* Port forward on 9001
* Create Airflow connection named s3_conn for Remote logging
  * Add Extra 
    `{"aws_access_key_id": "abhishek", "aws_secret_access_key": "choudhary123", "host": "http://minio:9000"}`
    Host is --endpoint_url and provide minio service http address
* 
