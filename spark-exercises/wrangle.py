from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()

def acquire_service_data():
    """Acquire 311 non-emergency service data
    and merge into single dataframe"""
    
    case = spark.read.csv("data/case.csv", sep=",",
                          header=True, inferSchema=True)
    dept = spark.read.csv("data/dept.csv", sep=",",
                          header=True, inferSchema=True)
    src = spark.read.csv("data/source.csv", sep=",",
                         header=True, inferSchema=True)
    
    #join
    df = case.join(src,
               on = case.source_id==src.source_id,
               how = 'left')\
                .join(dept,
                      on = case.dept_division==dept.dept_division,
                      how = 'left')\
                .drop(case.source_id).drop(case.dept_division)
    return df

def process_service_data():
    """Process 311 non-emergency service data,
    including new columns
    """
    
    df = acquire_service_data()
    
    #reformat dates
    fmt = "M/d/yy H:mm"
    df = df.withColumn("case_opened_date", to_timestamp("case_opened_date", fmt))\
            .withColumn("case_closed_date", to_timestamp("case_closed_date", fmt))\
            .withColumn("SLA_due_date", to_timestamp("SLA_due_date", fmt))
    
    #add columns
    df = df.withColumn('case_closed', expr('case_closed=="YES"'))\
            .withColumn('case_late', expr('case_late="YES"'))\
            .withColumn('request_address', trim(lower(df.request_address)))\
            .withColumn('year', year('case_closed_date'))\
            .withColumn('num_weeks_late', expr('num_days_late/7'))\
            .withColumn('zipcode', regexp_extract('request_address', r"(\d+$)",1))\
            .withColumn('council_district',col('council_district').cast('string'))\
            .withColumn('council_district', 
                        format_string('%03d', col('council_district').cast('int')))\
            .withColumn("case_age", datediff(current_timestamp(), "case_opened_date"))\
            .withColumn("days_to_closed", datediff("case_closed_date", "case_opened_date"))\
            .withColumn("case_lifetime", when(expr("! case_closed"),
                                        col("case_age")).otherwise(col("days_to_closed")))\
            .withColumnRenamed("standardized_dept_name", "department")
    return df