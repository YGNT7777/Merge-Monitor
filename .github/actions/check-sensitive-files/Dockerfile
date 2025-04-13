# .github/actions/check-sensitive-files/Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container, ensuring it exists
WORKDIR /action

# Ensure the /action directory exists before copying
RUN mkdir -p /action

# Install the necessary dependencies
RUN pip install --no-cache-dir requests

# Run the Python script when the container is started
ENTRYPOINT ["python", "./check-sensitive-files"]
