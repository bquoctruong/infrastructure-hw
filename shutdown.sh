#!/bin/bash

kubectl delete -f deployment.yaml

minikube pause

minikube stop