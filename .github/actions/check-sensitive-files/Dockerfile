# .github/actions/check-sensitive-files/Dockerfile
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /action

# Copy the necessary files into the Docker image from the repository root
COPY ../lockedFiles.txt ./

# Copy check.py (since it is inside the action directory)
COPY check.py ./

# Debugging: List files inside the directory after copying
RUN echo "Listing files in /action:" && ls -la /action

# Install the necessary dependencies
RUN pip install --no-cache-dir requests

# Debugging: Ensure that pip installed correctly
RUN echo "Checking installed packages:" && pip freeze

# Set the entry point to your Python script
ENTRYPOINT ["python", "check.py"]
