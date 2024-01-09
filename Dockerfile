# Use an official Python runtime as a base image
FROM python:3.9-buster

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install TTS
RUN pip install runpod==0.9.10

# Copy the rest of your app's source code from your host to your image filesystem.
COPY app/ .

# Run the web server on container startup
CMD ["python", "./main.py"]
