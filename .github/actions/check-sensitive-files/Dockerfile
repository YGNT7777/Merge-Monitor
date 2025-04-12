# .github/actions/check-sensitive-files/Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /action

# Copy the necessary files into the Docker image
COPY check.py ./  # Copy check.py into the working directory inside the container
COPY lockedFiles.txt ./  # Copy lockedFiles.txt into the working directory inside the container

# Install the necessary dependencies
RUN pip install --no-cache-dir requests

# Run the Python script when the container is started
ENTRYPOINT ["python", "check.py"]
