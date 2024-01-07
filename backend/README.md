# OpenCV Backend API Documentation
This API provides a simple endpoint for detecting people in an image using OpenVINO. The API is implemented using Flask, a Python web framework. </br>
</br>
## **API Endpoints** </br>
**1. Detect People** </br>
**- Endpoint: /detect_people** </br>
**- Method:** POST </br>
**- Description:** Detects people in the provided image and returns the bounding boxes as a JSON response. </br>
</br>
**Request** </br>
**- Content Type:** Multipart Form Data </br>
**- Parameters:** </br>
**-- 'image' (File): The input image file for people detection. </br>
</br>
**- Response** </br>
**- Content Type:** JSON </br>
**- Attributes:** </br>
**-- 'result' (String): Success or Error. </br>
**-- 'bounding_boxes' (List): List of dictionaries containing bounding box information for detected people. </br>
</br>
## **Payload Format** </br>

**Request Payload** </br>
**Method:** POST </br>
**URL:** http://your-api-base-url/detect_people </br>
**Headers:** None </br>
**Body:** Multipart form data </br>
**image:** Image file (JPEG, PNG, etc.) </br>
</br>
**Response Payload** </br>
**Content Type:** JSON </br>
**Attributes:** </br>
**result:**  "success" or "error". </br>
**bounding_boxes:** bounding boxes around detected people. </br>

## **Dependencies** </br>
(but the dependencies will be automatically installed if you used the docker option, in which the dependencies are already stated in the Dockerfile for the backend)</br>
### **1. Operating System: This Dockerfile is based on the ```python:3.8-slim``` image, which uses Debian Slim as the base operating system.** </br>
### **2. System Libraries:** </br>
- libgl1-mesa-glx </br>
- libglib2.0-0 </br>
### **3. Python Packages:** </br>
- opencv-python </br>
- openvino </br>
- flask </br>
- requests </br>
- numpy </br>
</br>
**Running the API** </br>
To run the API, execute the detect_people.py script directly. The Flask app will be hosted on **http://0.0.0.0:5000** by default.
