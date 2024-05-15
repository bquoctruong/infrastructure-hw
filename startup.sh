#!/bin/bash

# Function show_help to display options
show_help() {
    echo "Usage: $0 [-s]"
    echo "Options:"
    echo "  -m    Start minikube and set Docker environment"
}

# Minikube flag
minikube=false

# Options
while getopts ":h:m" opt; do
    case ${opt} in
        m )
            minikube=true
            ;;
        h )
            show_help
            exit 1
            ;;
    esac
done

# Start minikube and set Docker environment if flag is set
if [ "$minikube" = true ]; then
    minikube start --driver=docker
    eval $(minikube docker-env)
fi

./build-dockerfile.sh

kubectl apply -k kustomize/overlays/local/

sleep 10

kubectl port-forward svc/python-server-service 65432:65432 & minikube service python-server-service &
