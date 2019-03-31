#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys
print(sys.path)

import platform
print(platform.python_version())


from pyspark.sql import SparkSession

from share.foo import foo

spark_sc = SparkSession.builder.appName("testapp").getOrCreate()
log4jLogger = spark_sc._jvm.org.apache.log4j
logger = log4jLogger.LogManager.getLogger(__name__)

input_file = sys.argv[1]
output_folder = sys.argv[2]

df = spark_sc.read.json(input_file)
df.printSchema()
df.write.parquet(output_folder)

# use packages.
foo()
