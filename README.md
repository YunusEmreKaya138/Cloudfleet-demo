# Horizontal Scalability and Multi Cloud

This repository provides an example for demonstrating horizontal scalability and multi-cloud architecture. It includes:

A MongoDB server setup as a sample database layer across cloud environments.

A CPU stress test application to simulate load, helping illustrate how horizontal scaling behaves under pressure.

Use this project to observe how your system reacts when deployed across multiple nodes or cloud providers and how additional instances can help handle increased demand.

The Dockerfile is included in this repository.
You can either build and push the image to your own Docker Hub account, or pull it directly from the existing public repository if preferred.

````bash
kubectl apply -f ./yaml_files/deployment.yaml
````

````bash
kubectl apply -f ./yaml_files/mongo-deploy.yaml
````
