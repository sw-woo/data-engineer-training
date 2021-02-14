package main.scala.mnm
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

object MnmCount {

  def main(args: Array[String]) {
    val spark = SparkSession.builder.appName("M&M Count").getOrCreate()
    val mnm_df = spark.read.option("inferSchema", "true").option("header", "true").csv("data/mnm_dataset.csv")
    val count_mnm_df = mnm_df.select("State", "Color", "Count").groupBy("State", "Color").agg(count("Count").alias("Total")).orderBy(desc("Total"))
    count_mnm_df.show(30)
    println("Total Rows = {}".format(count_mnm_df.count()))

    val ca_count_mnm_df = mnm_df.select("Color", "Count").groupBy("Color").agg(count("Count").alias("Total_CA")).orderBy(desc("Total_CA"))
    ca_count_mnm_df.show(10)
    spark.stop()
  }

}
