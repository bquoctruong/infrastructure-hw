# README

This is a README for the ML Infrastructure Homework.

# Instructions

## Windows 10 + WSL2/Chromium Based Browser

### Pre-requisites
1. Install WSL2 [here](https://learn.microsoft.com/en-us/windows/wsl/install)
2. Install Docker Desktop [here](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module)
3. Open a WSL terminal
4. Install minikube [here](https://minikube.sigs.k8s.io/docs/start/)

### Quick Startup
1. `git clone https://github.com/bquoctruong/infrastructure-hw.git`
2. `cd infrastructure-hw`
3. `./startup.sh` or `./startup.sh -m` to start/enable minikube
4. Open address displayed in terminal in browser (ex. [default python-server-service  http://127.0.0.1:12345)

### Quick Shutdown
1. `CTRL + C`
2. `./shutdown.sh` or `./shutdown.sh -m` to stop minikube

### Startup (Commands taken from startup.sh)
1. `minikube start --driver=docker`
2. `eval $(minikube docker-env)`
3. `./build-dockerfile.sh`
4. `kubectl apply -k kustomize/overlays/local/`
5. `kubectl port-forward svc/python-server-service 65432:65432 & minikube service python-server-service &`
6. Open web browser (Chromium-based)
7. Navigate to address displayed in terminal (ex. [default python-server-service  http://127.0.0.1:12345)

### Shutdown (Commands taken from shutdown.sh)
1. `kubectl delete -k kustomize/overlays/local/`
2. `minikube pause`
3. `minikube stop`

### Additional Support
You may substitute Kustomize by utilizing the deployment.yaml file located at the root of the directory. Replace the above `apply/delete` commands with the respective command:

`kubectl apply -f deployment.yaml`
`kubectl delete -f deployment.yaml`
