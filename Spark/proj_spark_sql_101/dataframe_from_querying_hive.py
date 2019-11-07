from pyspark.sql import SparkSession

if __name__ == "__main__":
    # Create SparkSession
    spark = SparkSession \
        .builder \
        .enableHiveSupport() \
        .getOrCreate()

    spark.sql("show tables").show()

    spark.sql("describe page_views").show()
    spark.sql("describe formatted page_views").show(truncate=False)

    # query page_views table
    counts_by_os = spark.sql("select os, count(*) as total from page_views group by os")
    counts_by_os.show()

