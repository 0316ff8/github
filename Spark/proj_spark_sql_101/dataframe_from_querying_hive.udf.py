from pyspark.sql import SparkSession

if __name__ == "__main__":
    # Create SparkSession
    spark = SparkSession \
        .builder \
        .enableHiveSupport() \
        .getOrCreate()

    spark.sql("show tables").show()

    # using UDF
    spark.sql("add jar /home/cloudera/IdeaProjects/proj_hive_udf/out/artifacts/hive_udf/hive_udf.jar")
    spark.sql("create temporary function revs as 'com.iii.udf.MyReverse'")

    spark.sql("SELECT os, revs(os) as rev_os FROM page_views").show()

    # audi case study
    spark.sql("ADD FILE /home/cloudera/Desktop/hive_in_practice/audi/region_template/qk_cn.csv")
    spark.sql("ADD JAR /home/cloudera/IdeaProjects/proj_hive_udf/out/artifacts/hive_udf/hive_udf.jar")
    spark.sql("ADD JAR /home/cloudera/IdeaProjects/proj_hive_udf/libs/quadkey_utils.jar")
    spark.sql("CREATE TEMPORARY FUNCTION get_geo_locations AS 'com.iii.udf.GetGeoLocations'")

    result = spark.sql("""
                        SELECT ad_id, region,SUM(imp),COUNT(DISTINCT imp_imei),SUM(click),COUNT(DISTINCT click_imei)
                        FROM
                        (
                        SELECT
                        ad_id,
                        region,
                        CASE WHEN log_type=1 THEN 1 ELSE 0 END AS imp,
                        CASE WHEN log_type=1 THEN imei ELSE null END AS imp_imei,
                        CASE WHEN log_type=2 THEN 1 ELSE 0 END AS click,
                        CASE WHEN log_type=2 THEN imei ELSE null END AS click_imei
                        FROM report_input
                        LATERAL VIEW explode(split(get_geo_locations(ip_quadkey),',')) subview AS region
                        ) src
                        GROUP BY ad_id, region""")

    result.show(100)

