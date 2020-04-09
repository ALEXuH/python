from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("aaa") \
    .enableHiveSupport() \
    .master("local[2]") \
    .config("spark.sql.codegen", True) \
    .getOrCreate()
#spark.createDataFrame

