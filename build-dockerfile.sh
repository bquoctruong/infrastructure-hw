#!/bin/bash

docker build -t ml-hw-python-server:latest -f python_server/Dockerfile python_server/
docker build -t ml-hw-python-client:latest -f python_client/Dockerfile python_client/