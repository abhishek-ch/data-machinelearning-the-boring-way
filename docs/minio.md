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
