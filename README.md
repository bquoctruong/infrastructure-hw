# README

This is a README for the ML Infrastructure Homework.

# Instructions

## Windows 10 + WSL2/Chromium Based Browser

### Pre-requisites
1. Install WSL2 [here](https://learn.microsoft.com/en-us/windows/wsl/install)
2. Install Docker Desktop [here](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module)
3. Open a WSL terminal
4. Install minikube [here](https://minikube.sigs.k8s.io/docs/start/)

### Startup
1. `git clone https://github.com/bquoctruong/infrastructure-hw.git`
2. `cd infrastructure-hw`
3. `./startup.sh`
4. Open address displayed in terminal in browser (ex. [default python-server-service  http://127.0.0.1:12345)

### Shutdown
1. `CTRL + C`
2. `./shutdown.sh`
