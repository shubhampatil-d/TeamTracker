# Dockerfile

# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Run Django server
CMD ["gunicorn", "taskflow.wsgi:application", "--bind", "0.0.0.0:8000"]
