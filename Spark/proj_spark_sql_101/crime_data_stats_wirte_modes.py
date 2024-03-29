from pyspark.sql import SparkSession
from pyspark.sql.functions import *

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Crime Data") \
        .getOrCreate()

    data = spark.read.csv(header=True, path="hdfs://localhost/user/cloudera/spark_sql_101/crime/data/")
    data.printSchema()
    data.show()
    data.count()
    data.describe().show()

    crime_2015_6 = data.filter("year >= 2015").drop("lsoa_code")
    crime_2015_6.show()

    convictions_by_borough = crime_2015_6.groupBy("borough").agg({"value": "sum"})
    convictions_by_borough.show()

    convictions_by_borough = convictions_by_borough.withColumnRenamed("sum(value)", "num_of_convictions")
    convictions_by_borough.show()

    total_convictions = convictions_by_borough.agg({"num_of_convictions": "sum"}).collect()[0][0]
    convictions_by_borough_with_percentage = convictions_by_borough.withColumn("percentage_convictions",
                            format_number(convictions_by_borough["num_of_convictions"] / total_convictions * 100, 2))

    convictions_by_borough_with_percentage.cache()

    # show result of 100 records to console
    convictions_by_borough_with_percentage.show(100)

    # write result to Hive Table convictions_by_borough_with_percentage
    convictions_by_borough_with_percentage.write.saveAsTable("default.convictions_by_borough_with_percentage")


    # write result to MySQL Table convictions_by_borough_with_percentage
    convictions_by_borough_with_percentage.write \
                                          .option("driver", "com.mysql.jdbc.Driver") \
                                          .jdbc("jdbc:mysql://localhost:3306", "crime.convictions_by_borough_with_percentage",
                                                  properties={"user": "root", "password": "cloudera"})
