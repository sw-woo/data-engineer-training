#!/bin/bash
# Supress info w/ $SPARK_HOME/conf/log4j.properties INFO -> ERROR
SPARK_HOME="/Users/psyoblade/Downloads/spark-3.0.1-bin-hadoop2.7"
$SPARK_HOME/bin/spark-submit $1
