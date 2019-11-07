from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

if __name__ == "__main__":

    spark = SparkSession \
        .builder \
        .getOrCreate()

    slen = udf(lambda s: len(s), IntegerType())

    df = spark.read.csv("hdfs://localhost/user/cloudera/spark_sql_101/data/stocks_header.txt", inferSchema=True,
                        header=True)

    df.printSchema()
    df.show()

    df.select(slen("symbol").alias("length_of_symbol")).show()

    df.createOrReplaceTempView("stocks")

    spark.udf.register("slen2", lambda s: len(s), IntegerType())

    spark.sql("select slen2(symbol) as length_of_symbol from stocks").show()
