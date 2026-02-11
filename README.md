# Python System Monitor (Dockerized) 

A simple application for monitoring system parameters, running inside a Docker container. This is an educational project created to learn the basics of containerization.

## 🚀 Technologies
* **Python 3.13**
* **Docker**
* **Linux** (container environment)

## 📋 Prerequisites
Before you begin, ensure you have the following installed on your local machine:
* [Docker](https://docs.docker.com/get-docker/)

## 🛠 How to Run

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/VladyslavKorniichuk/python-system-monitor-docker.git
   cd python-system-monitor-docker

2. **Build the Docker image**:
   Make sure you are in the project folder, and run this command:
   ```bash
   docker build -t system-monitor . 
  
3. **Run the container**:
   Start the system monitor. Run the following command to start it in the background:
   ```bash
   docker run -d --name sys-monitor system-monitor

4. **View the live logs**:
   Since the container is running in the background, you will need to check its logs to see the system monitoring data in real-time. Run this command:
   ```bash
   docker logs -f sys-monitor

5. **Stop and clean up**:
   When you are done testing the monitor, you can safely stop the container and remove it to free up resources:
   ```bash
   docker stop sys-monitor
   docker rm sys-monitor
