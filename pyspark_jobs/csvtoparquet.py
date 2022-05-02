import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from sessionbuilder import *


def main(source_path: str, destination_path: str) -> DataFrame:
    _logger.info(f'Reading from CSV Path {source_path}')
    dataframe = spark.read.format("csv").option(
        "header", "true").load(source_path)
    dataframe_cast = dataframe.withColumn("account_created_at", to_date(col("account_created_at"),"yyyy-MM-dd HH:mm:ss")) \
        .withColumn("account_created_at_interpolated", to_date(col("account_created_at_interpolated"),"yyyy-MM-dd HH:mm:ss"))
    _logger.info(f'TESTING ABC...')
    _logger.info(f'CSV As DataFrame {dataframe_cast.show()}')
    dataframe_cast.printSchema()

    dataframe_cast.coalesce(1) \
        .write \
        .format("parquet") \
        .save(destination_path, mode="overwrite")

    return dataframe


if __name__ == '__main__':
    source_path = sys.argv[1]
    destination_path = sys.argv[2]
    print(
        f'User Input Source Path {source_path} Write Path {destination_path}')
    spark, _logger = get_new_session("CSV To Parquet")

    main(source_path=source_path, destination_path=destination_path)
    spark.stop()
