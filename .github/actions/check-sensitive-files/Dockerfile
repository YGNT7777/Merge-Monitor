# .github/actions/check-sensitive-files/Dockerfile
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /action

# Copy necessary files into the Docker image
COPY check.py lockedFiles.txt ./

# Debugging: List files inside the directory after copying
RUN echo "Listing files in /action:" && ls -la /action

# Install the necessary dependencies
RUN pip install --no-cache-dir requests

# Debugging: Ensure that pip installed correctly
RUN echo "Checking installed packages:" && pip freeze

# Set the entry point to your Python script
ENTRYPOINT ["python", "check.py"]
