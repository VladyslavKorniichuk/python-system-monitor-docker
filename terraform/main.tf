# Terraform configuration to set up a monitoring server on AWS
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Specify the AWS region where resources will be created
provider "aws" {
  region = "eu-central-1"
}

# Create a security group for the monitoring server
resource "aws_security_group" "monitor_sg" {
  name        = "monitor_sg"
  description = "Allow port 8000 for App and 22 for SSH"

  # Allow incoming traffic on port 8000
  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow incoming traffic on port 22 (SSH)
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outgoing traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create the monitoring server instance
resource "aws_instance" "monitor_server" {
  ami           = "ami-07e02d61816ed19e2" 
  instance_type = "t2.micro"              
  
  vpc_security_group_ids = [aws_security_group.monitor_sg.id]

  # User data script to set up Docker and run the container
  user_data = <<-EOF
              #!/bin/bash
              apt-get update -y
              apt-get install -y docker.io
              systemctl start docker
              systemctl enable docker

              docker run -d \
                -p 8000:8000 \
                --name sys-monitor \
                --restart unless-stopped \
                ghcr.io/vladyslavkorniichuk/python-system-monitor-docker:latest
              EOF

  tags = {
    Name = "PythonMonitorServer"
  }
}

# Output the public IP of the monitoring server
output "server_public_ip" {
  description = "Public IP of the Monitoring Server"
  value       = aws_instance.monitor_server.public_ip
}