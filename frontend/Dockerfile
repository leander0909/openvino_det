# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install necessary dependencies for OpenCV
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/frontend

# Install any needed packages specified in requirements.txt
RUN pip install -r /app/frontend/requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run frontend.py when the container launches
CMD ["python", "/app/frontend/frontend.py"]
