#!/bin/bash

# =========================================================
# deployment script for AWS EC2
# This script is triggered by the GitHub Actions workflow
# =========================================================

# Exit immediately if a command exits with a non-zero status
set -e

echo "Starting Deployment process..."

# Define your project root here (where you cloned your repo on EC2)
# Often this is /home/ubuntu/sbi-lms
PROJECT_DIR="/home/ubuntu/sbi-lms"
VIRTUAL_ENV_DIR="/home/ubuntu/sbi-lms/venv"

echo "Navigating to project directory: $PROJECT_DIR"
cd $PROJECT_DIR

echo "Pulling latest code from GitHub..."
git fetch origin main
git reset --hard origin/main

echo "Activating virtual environment..."
source $VIRTUAL_ENV_DIR/bin/activate

echo "Installing upgraded Python dependencies..."
pip install -r requirements.txt

echo "Running Database Migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Restarting Gunicorn Service..."
# Adjust the service name if you named your gunicorn service differently
sudo systemctl daemon-reload
sudo systemctl restart gunicorn

echo "Restarting Nginx Service..."
sudo systemctl restart nginx

echo "Deployment completed successfully!"
