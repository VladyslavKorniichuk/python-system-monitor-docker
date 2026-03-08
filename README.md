# Python System Monitor (Dockerized) 

[![Docker CI/CD](https://github.com/VladyslavKorniichuk/python-system-monitor-docker/actions/workflows/ci.yml/badge.svg)](https://github.com/VladyslavKorniichuk/python-system-monitor-docker/actions/workflows/ci.yml)

A lightweight, containerized Python application that monitors real-time system metrics (CPU, RAM, Disk usage) and displays them via a live-updating Web UI. Built as an educational project to learn Docker, CI/CD pipelines, and web development basics.

## 🌟 Features
* **Live Dashboard**: A dark-themed web UI that updates metrics automatically every 2 seconds via JavaScript.
* **REST API**: Serves raw system metrics in JSON format via the `/data` endpoint.
* **Continuous Deployment**: Automated builds pushed to GitHub Container Registry (GHCR) using GitHub Actions.
* **Optimized & Secure**: Uses a minimal `python:3.13-slim` base image and includes a built-in Docker `HEALTHCHECK`.

## 🚀 Technologies
* **Python 3.13** (with `psutil` for hardware metrics)
* **HTML / CSS / Vanilla JS** (Frontend)
* **Docker & Docker Compose** (Containerization)
* **GitHub Actions** (CI/CD Pipeline)
* **Ruff** (Lightning-fast Python linter)

## 📋 Prerequisites
Before you begin, ensure you have the following installed on your local machine:
* [Docker](https://docs.docker.com/get-docker/)

## 🛠 Quick Start (Run from GHCR)
You don't even need to clone the repository! You can run the pre-built image directly from the GitHub Container Registry:

```bash
docker run -d -p 8000:8000 --name sys-monitor ghcr.io/vladyslavkorniichuk/python-system-monitor-docker:latest
```
Once the container is running, open your browser and navigate to http://localhost:8000.

## 💻 Local Development
If you want to build and modify the code locally, follow these steps:

1. **Clone the repository**:
```bash
git clone [https://github.com/VladyslavKorniichuk/python-system-monitor-docker.git](https://github.com/VladyslavKorniichuk/python-system-monitor-docker.git)
cd python-system-monitor-docker
```

2. **Build and run using Docker Compose**:
```bash
docker-compose up -d --build
```

3. **View the dashboard:**
Open http://localhost:8000 in your web browser. To see the raw JSON data, go to http://localhost:8000/data.

4. **View the live logs (Optional)**:
```bash
docker logs -f sys-monitor
```

5. **Stop and clean up**:
```bash
docker-compose down
```
