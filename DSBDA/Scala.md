Step 1: Check if java is available if not then download
```
sudo apt update
sudo apt install openjdk-11-jdk
java -version
```

Step 2: Download Apache Spark

    Go to the Apache Spark download page: Apache Spark Downloads.

    Choose a version and download the pre-built Hadoop package. For simplicity, let’s say you’re downloading the Spark 3.x version with Hadoop 3.x.

    You can use wget or download the .tar.gz file manually from the website.

    Example using wget:

    `wget https://dlcdn.apache.org/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3.tgz`

Step 3: Extract Apache Spark

Once you’ve downloaded the .tar.gz file, you’ll need to extract it:

`tar -xvzf spark-3.4.0-bin-hadoop3.tgz`

This will extract the Spark files into a folder named spark-3.4.0-bin-hadoop3 in your current directory.
Step 4: Set Environment Variables

We need to set the SPARK_HOME variable and update the PATH to include Spark's bin directory.

    Open your ~/.bashrc file for editing (or ~/.bash_profile if on macOS or using a different shell):

`nano ~/.bashrc`

Add the following lines at the end:
```
export SPARK_HOME=~/spark-3.4.0-bin-hadoop3
export PATH=$PATH:$SPARK_HOME/bin
```

Note: Adjust the SPARK_HOME path to match the location where you extracted Spark.

After editing, save and exit by pressing CTRL+X, then Y to confirm changes.

Reload the .bashrc file to apply the changes:

    `source ~/.bashrc`

Step 5: Start the Spark Shell

Now that you’ve set everything up, you can try starting the spark-shell:

    `spark-shell`

Step 6: Download Scala

```
sudo  apt install scala 
scala -version
```



Create a file:
 `nano filename.scala`

`object filename{
   def main(args: Array[String]): Unit ={
        println(" Helloo")}}
`

Compile 

`scalac filename.scala`

Run

`scala filename`


NOTE: OBJECT SHOULD BE SAME AS YOUR FILENAME

code for wordCount:

```
import org.apache.spark.sql.SparkSession

object WordCount {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder
      .appName("Simple WordCount")
      .master("local[*]") // run locally
      .getOrCreate()

    val sc = spark.sparkContext

    val textFile = sc.textFile("input.txt")  // Your input file

    val counts = textFile.flatMap(line => line.split(" "))
                         .map(word => (word, 1))
                         .reduceByKey(_ + _)

    counts.collect().foreach(println)

    spark.stop()
  }
}
```

Save the file & Compile:
`scalac -classpath "C:\spark\jars\*" WordCount.scala`
