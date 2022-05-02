import sys
from pyspark.sql.functions import *
from pyspark.sql.types import *
from sessionbuilder import *
import json
from pathlib import Path


def main(source_path: str, destination_path: str) -> bool:
    dataframe = spark.read.parquet(source_path) \
        .withColumn("year", year("account_created_at")) \
        .withColumn("month", month("account_created_at")) \
        .withColumn("day", dayofmonth("account_created_at"))

    dataframe.coalesce(1) \
        .write \
        .format("parquet") \
        .partitionBy("year", "month", "day") \
        .save(destination_path, mode="overwrite")

    return True


def push_to_xcom(destination_path: str) -> None:
    # Path("/airflow/xcom/").mkdir(parents=True, exist_ok=True)
    with open("/airflow/xcom/return.json", 'w') as file:
        logging.info(f'XCom Push {destination_path}')
        json.dump(destination_path, file)

    data = json.load(open("/airflow/xcom/return.json"))
    logging.info(data)


if __name__ == '__main__':
    source_path = sys.argv[1]
    destination_path = sys.argv[2]

    spark, _logger = get_new_session("CSV To Parquet")
    push_to_xcom(destination_path)
    _logger.info(
        f'Parquet Source Path {source_path} Write Path {destination_path}')

    if main(source_path, destination_path):
        push_to_xcom(destination_path)

    spark.stop()
