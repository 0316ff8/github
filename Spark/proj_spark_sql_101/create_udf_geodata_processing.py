from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from geoip2.database import Reader # assume all work nodes have geoip2 installed

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("GeoData") \
        .getOrCreate()

    reader = None

    def ip2city_py(ip):
        global reader
        if reader is None:
            # assume all work nodes have mmdb installed in the following path
            reader = Reader("/home/cloudera/Desktop/spark_sql_101/maxmind/GeoLite2-City.mmdb")
        try:
            response = reader.city(ip)
            city = response.city.name
            if city is None:
                return None
            return city

        except:
            return None

    ip2city= udf(ip2city_py, StringType())

    page_view = spark.sql("select * from page_views")
    page_view_city = page_view.withColumn("city", ip2city("ip"))
    page_view_city.show()

    # assume quadkey_tekplate_db and qk_cn are not present in worker nodes
    spark.sql("add file /home/cloudera/PythonProjects/proj_spark_sql_101/quadkey_template_db.py")
    spark.sql("add file /home/cloudera/Desktop/spark_sql_101/region_template/qk_cn.csv")

    from quadkey_template_db import QuadkeyTemplateDB

    qkDB = None

    def get_locations_py(quadkey):
        global qkDB
        if qkDB is None:
            qkDB = QuadkeyTemplateDB("./qk_cn.csv")
        found = qkDB.lookup_regions(quadkey)
        if len(found) != 0:
            return found
        else:
            return ["NotFound"]


    get_locations = udf(get_locations_py, ArrayType(StringType()))

    report_input = spark.sql("select * from report_input")
    report_input.printSchema()
    report_input.show()

    report_input.select(get_locations("ip_quadkey")).show()

    result = report_input.select("ad_id", explode(get_locations("ip_quadkey")).alias("region"), "log_type", "imei") \
        .withColumn("imp", when(report_input["log_type"] == 1, 1).otherwise(0)) \
        .withColumn("imp_imei", when(report_input["log_type"] == 1, report_input["imei"]).otherwise(None)) \
        .withColumn("click", when(report_input["log_type"] == 2, 1).otherwise(0)) \
        .withColumn("click_imei", when(report_input["log_type"] == 2, report_input["imei"]).otherwise(None)) \
        .groupBy("ad_id", "region").agg(sum("imp"), countDistinct("imp_imei"), sum("click"),countDistinct("click_imei")) \

    result.orderBy(result["sum(click)"].desc()).show()
