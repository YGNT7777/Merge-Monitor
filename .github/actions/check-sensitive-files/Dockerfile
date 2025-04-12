# .github/actions/check-sensitive-files/Dockerfile
FROM python:3.x

# Set the working directory inside the container
WORKDIR /action

# Copy your Python script and any required files to the container
COPY check.py lockedFiles.txt ./

# Install the necessary dependencies
RUN pip install requests

# Set the entry point to your Python script
ENTRYPOINT ["python", "check.py"]
