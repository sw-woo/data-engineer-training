#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("M&M Count").getOrCreate()
mnm_df = spark.read.option("inferSchema", "true").option("header", "true").csv("data/mnm_dataset.csv")
count_mnm_df = mnm_df.select("State", "Color", "Count").groupBy("State", "Color").agg(count("Count").alias("Total")).orderBy("Total", ascending=False)
count_mnm_df.show(n=30, truncate=False)
print("Total Rows = {}".format(count_mnm_df.count()))

ca_count_mnm_df = mnm_df.where(expr("State = 'CA'")).select("Color", "Count").groupBy("Color").agg(count("Count").alias("Total_CA")).orderBy("Total_CA", ascending=False)
ca_count_mnm_df.show(n=10, truncate=False)

spark.stop()
