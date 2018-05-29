# Spark Cluster Deployment and Computing with PySpark
Currently, the project makes some assumptions about its environment:
- The computing nodes can connect via password-less ssh tunneling
- Spark is not already installed on the cluster.
    - If you have spark installed and just want to connect with pyspark, simply run the import statements and environment config. Then, import pyspark and initiate the spark session.

Run the setup notebook to install spark. Then feel free to explore the examples for reference.

The cluster is hosted in Google Cloud.
