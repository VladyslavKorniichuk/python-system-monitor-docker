# Python System Monitor (Dockerized) 

[![Docker CI/CD](https://github.com/VladyslavKorniichuk/python-system-monitor-docker/actions/workflows/ci.yml/badge.svg)](https://github.com/VladyslavKorniichuk/python-system-monitor-docker/actions/workflows/ci.yml)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

A lightweight, containerized Python application that monitors real-time system metrics (CPU, RAM, Disk, Network I/O, Uptime) and displays them via a live-updating Web UI. Built as an educational project to learn Docker, CI/CD pipelines, Infrastructure as Code, and web development basics.

## 🌟 Features
* **Live Dashboard**: A dark-themed web UI that updates metrics automatically every 2 seconds via JavaScript Fetch API.
* **REST API**: Serves raw system metrics in JSON format via the `/data` endpoint.
* **Production-Ready Docker**: Utilizes multi-stage builds, runs as a non-root user for security, and includes a built-in `HEALTHCHECK`.
* **CI/CD Pipeline**: Automated code linting (Ruff) and image builds pushed to GitHub Container Registry (GHCR) using GitHub Actions.
* **Full Continuous Deployment**: Integrated `Watchtower` in `docker-compose.yml` for zero-downtime automated container updates.
* **Infrastructure as Code (IaC)**: Includes `Terraform` configuration to automatically provision AWS EC2 instances and deploy the container.

## 🚀 Technologies
* **Python 3.13** (with `psutil` for hardware metrics)
* **HTML / CSS / Vanilla JS** (Frontend)
* **Docker & Docker Compose** (Containerization & Orchestration)
* **GitHub Actions** (CI/CD Pipeline)
* **Terraform** (AWS Infrastructure Provisioning)
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
