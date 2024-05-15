#!/bin/bash

# Function show_help to display options
show_help() {
    echo "Usage: $0 [-s]"
    echo "Options:"
    echo "  -m    Stop minikube"
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

kubectl delete -k kustomize/overlays/local/

# Stop minikube if flag is set
if [ "$minikube" = true ]; then
    minikube pause
    minikube stop
fi