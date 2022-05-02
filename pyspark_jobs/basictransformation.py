import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from sessionbuilder import *

def main():
    pass

if __name__ == '__main__':
    source_path = sys.argv[1]
    destination_path = sys.argv[2]
    print(
        f'User Input Source Path {source_path} Write Path {destination_path}')
    spark, _logger = get_new_session("CSV To Parquet")

    main(source_path=source_path, destination_path=destination_path)
    spark.stop()