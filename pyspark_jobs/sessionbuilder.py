from pyspark.sql import SparkSession
import logging


def get_new_session(app_name):
    spark = SparkSession.builder.appName(app_name).getOrCreate()
    spark.conf.set("spark.sql.sources.partitionOverwriteMode", "dynamic")

    spark.sparkContext.setLogLevel("INFO")
    log4j = spark._jvm.org.apache.log4j.Logger
    _logger = log4j.getLogger(__name__)

    return (spark, _logger)
