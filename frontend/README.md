# **Frontend Documenation** </br>

## Usage </br>
**1. Access the Frontend:** </br>
- Open a web browser and navigate to http://localhost:80 to access the main index page. </br>

**2. Upload an Image:** </br>
- Click on the "Choose File" button to select an image for upload. </br>
- After selecting the image, click on the "Upload" button. </br>

**3. View Results:** </br>
- The uploaded image will be sent to the OpenVINO backend for processing. </br>
- Once processed, the frontend will display the result page with the processed image and bounding boxes around detected people. </br>

## **Code Explanation** </br>
The **frontend.py** script defines a Flask web application with the following main routes: </br>
- **/:** The main index page. </br>
- **/upload:** Handles image upload, sends it to the OpenVINO backend, and renders the result page. </br>
The Dockerfile installs the required dependencies (Flask and Requests) within the Docker image. </br>

## Dependencies
### 1. Operating System: This Dockerfile is based on the ```python:3.8-slim``` image, which uses Debian Slim as the base operating system.
### 2. Python Packages:
- opencv-python
- flask
- requests
- numpy

## **Important Note** </br>
Ensure that the OpenCV backend is running and accessible at the specified URL (http://backend:5000/detect_people) before using the frontend. Adjust the backend URL in the code if needed. </br>

## **Customization** </br>
Feel free to customize the frontend templates (index.html and result.html) to suit your application's design and branding. </br>

