#!/bin/bash

minikube start --driver=docker

eval $(minikube docker-env)

./build-dockerfile.sh

kubectl apply -f deployment.yaml

sleep 10

kubectl port-forward svc/python-server-service 65432:65432 & minikube service python-server-service &