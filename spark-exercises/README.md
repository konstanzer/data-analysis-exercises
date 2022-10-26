### Apache Spark Architecture

**Spark** is written in a language called Scala, which runs on the Java Virtual Machine (JVM.) Rather than write Scala code, you may use client libraries to interact with Spark. I'm using **pyspark**. Pyspark can manipulate Spark dataframes and translate Python into Scala that will run on the JVM. Because pyspark is interfacing with Spark, we will sometimes see Java error messages.

A Spark application consists of:

* The Driver, a JVM process, analyzes your program, optimizes queries, and **parallelizes** jobs.
    * All of the executors work together at the same time.
    * Within each executor, the data is divided into partitions equal to the number of CPU cores on the executor.
* The Cluster Manager allocates resources and schedules jobs on the cluster.
* The Executors perform the distributed work.

The Driver is usually on your laptop, which will be running pyspark and will be connected to a cluster. Spark may also run on a single machine through **local mode**. In local mode, there are no Executor processes. Instead, the Driver also acts as the sole Executor.

In this repo, I exclusively run spark in local mode in order to get familiar with the Spark API and writing pyspark code.

### Transformations, Actions, Shuffling

Spark dataframe manipulation has two categories:

* Transformations: function that selects a subset of the data and transforms, reorders, or aggregates the data
* Actions: transformations *in action*, for example, actually counting the rows or viewing the first record

Spark is **lazy**. We can specify many transformations but they'll be applied when we specify an action.

A **shuffle** occurs when an action requires data in another partition or executor.

* Arithmetic: no shuffle (each number can be processed independently.)
* Sorting: shuffle (the order is determined by all data.)
* Subsetting: no shuffle (each row can be processed independently.)
* Averaging: shuffle (the average depends on all data.)

Shuffles are expensive. Determining when to shuffle is one of the largest considerations in optimizing Spark code.

### Install Dependencies

Run the following commands from your terminal:

    brew tap adoptopenjdk/openjdk
    brew cask install adoptopenjdk11

After running the commands above, you can run

    java -version

And you should see output similar to:

    openjdk version "11.0.4" 2019-07-16
    OpenJDK Runtime Environment AdoptOpenJDK (build 11.0.4+11)
    OpenJDK 64-Bit Server VM AdoptOpenJDK (build 11.0.4+11, mixed mode)

After java is installed, we can install pyspark, the library that provides the python interface to spark:

    python -m pip install pyspark
