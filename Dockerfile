# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set an environment variable with the build version and project name
ENV VERSION=0.1
ENV NAME=purrs

# Set the working directory in the container to /app
WORKDIR /app

# Set the Python path to include /app/src and /app/tests
ENV PYTHONPATH=/app/src:/app/tests

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the script when the container launches
CMD pytest && python -m src.reddit_rss
