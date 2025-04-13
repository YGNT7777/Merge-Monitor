# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /action

# Copy everything in the current directory (where Dockerfile is) into the container
COPY . /action

# Install the necessary dependencies
RUN pip install --no-cache-dir requests

# Run the Python script when the container is started
ENTRYPOINT ["python", "check.py"]
