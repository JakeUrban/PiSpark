# Spark Cluster Deployment and Computing with PySpark

This repository contains notebooks for downloading, installing, configuring, and using PySpark. I will detail instructions below for what you need to do before running setup_spark.ipynb, which assumes the computing nodes are connectable via ssh and have the necessary software packages to run the notebook's code.

Once spark is installed, configured, and functioning, feel free to explore the other spark examples, but I recommend reading spark_bag_of_words.ipynb as it has important configuration material that I had not yet known in the earlier notebooks. However, the spark configuration in the bag-of-words notebook is built in as a single-node cluster, so make sure you understand how normal configuration works before trying to understand something different.

I will teach you how to configure your computing nodes into a spark cluster. Once you understand how to do that, changing spark_bag_of_words to fit your cluster configuration should be trivial.

# Setting up Our Cloud Environment

Pick Google Cloud. Its easy to sign up and use, and it allows you to use 8 CPU's on it's free tier compared to Azure's 4 CPU's. I trust you can navigate to the computing instances UI and create Ubuntu or Debian linux boxes. Here is what I think you should create:

1 node with 2 CPU's and 8GB of memory, 10GB of disk.
2 nodes with 3 CPU's and 32GB each, 10GB of disk.

Apparently 5 cores per executor is ideal, but we only have 6 cores total so we'll go with 2 3-core nodes. You could have 3 nodes with 2 CPU's, or something else.

Next:

For the head node:
- Put your local computings public key in the head node's .ssh/authorized_keys file
- sudo apt-get update
- sudo apt-get install default-jre
- Add JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/jre" to .profile or .bashrc
- Add the internal network IP’s and hostnames of each node to /etc/hosts
- sudo apt-get install python-pip
- sudo apt-get install git
- git clone PiSpark
- pip install jupyter

For all nodes:
- Put the head node's public key (or generate it, if not there) in each worker node's .ssh/authorized_keys file
- sudo apt-get update
- sudo apt-get install default-jre
- Add JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/jre" to .profile or .bashrc
- Add the internal network IP and hostname of THIS NODE to /etc/hosts 
- sudo apt-get install python-pip
- pip install numpy

# Connecting to the Cluster

(On the head node)
~$ jupyter notebook --no-browser --port=8081

(On your local machine):
~$ ssh -N -L 8081:localhost:8081 user@hostname

This will create an ssh tunnel for the jupyter notebook you just launched. Go to https://localhost:8081 to use the notebook as usual. The notebook will take it from there.

