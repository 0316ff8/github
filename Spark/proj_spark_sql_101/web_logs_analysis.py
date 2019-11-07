from pyspark.sql import SparkSession, Row

def line_to_row(line):
    record = line.split(",")
    return Row(timestamp=record[0],
               referrer=record[1],
               action=record[2],
               visitor=record[3],
               page=record[4],
               product=record[5])


if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .getOrCreate()

    sc = spark.sparkContext

    logs_df = spark.createDataFrame(sc.textFile("hdfs://localhost/user/cloudera/spark_sql_101/ec/data").map(line_to_row))

    logs_df.createOrReplaceTempView("logs")

    visitorsByProduct = spark.sql(
      """SELECT substring(timestamp, 0, 10) as day, product, COUNT(DISTINCT visitor) as uu
         FROM logs 
         GROUP BY substring(timestamp, 0, 10), product
         ORDER BY day ASC, uu DESC
        """).persist()

    visitorsByProduct.show(100)
    visitorsByProduct.write.mode("overwrite").json("hdfs://localhost/user/cloudera/spark_sql_101/ec/ouptut/visitors_by_product")

    activityByProduct = spark.sql("""SELECT substring(timestamp, 0, 10) as day, product,
                                      sum(case when action = 'sale' then 1 else 0 end) as number_of_sales,
                                      sum(case when action = 'add_to_cart' then 1 else 0 end) as number_of_add_to_cart,
                                      sum(case when action = 'page_view' then 1 else 0 end) as number_of_page_views
                                      from logs
                                      group by substring(timestamp, 0, 10), product""").persist()
    activityByProduct.show(100)
    activityByProduct.write.mode("overwrite").parquet("hdfs://localhost:/user/cloudera/spark_sql_101/ec/ouptut/activity_by_product")
