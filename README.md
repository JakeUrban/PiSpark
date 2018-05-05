# Spark Cluster Deployment and Computing with PySpark
Currently, the project makes some assumptions about its environment:
- The cluster is a network of 3 raspberry pi's.
- The computing nodes can connect via password-less ssh tunneling
- Spark is not already installed on the cluster.
    - If you have spark installed, running, and just want to connect with pyspark, simply run the import statements and environment config. Then, import pyspark and initiate the spark session.

Later iterations of this code will be built for a public cloud environment.
