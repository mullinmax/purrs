# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Set the Python path to include /app so it includes src and tests
ENV PYTHONPATH=/app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Ensure that the database is properly initialized before starting the server
RUN python -c "from src.database.session import init_db; init_db()"

# Run the flask app
CMD ["python", "-m", "waitress", "-b", "0.0.0.0:5000", "main:app"]
