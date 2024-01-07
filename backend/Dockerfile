# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install necessary dependencies for OpenCV
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/backend

# Create a model directory if it doesn't exist and copy the model files into it
COPY model /app/backend/model

# Install any needed packages specified in requirements.txt
RUN pip install -r /app/backend/requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run backend.py when the container launches
CMD ["python", "/app/backend/person_det.py"]
