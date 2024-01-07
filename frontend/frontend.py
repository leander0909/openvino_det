from flask import Flask, render_template, request, jsonify, send_file
import requests
import cv2
import numpy as np
import base64
from io import BytesIO

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for handling file uploads
@app.route('/upload', methods=['POST'])
def upload():
    # Check if 'file' is present in the uploaded files
    if 'file' not in request.files:
        return render_template('index.html', message='No file part')

    file = request.files['file']

    # Check if a file was selected
    if file.filename == '':
        return render_template('index.html', message='No selected file')

    if file:
        # Read the image and resize if its width is greater than 640 pixels
        image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
        if image.shape[1] > 640:
            scale_factor = 640 / image.shape[1]
            image = cv2.resize(image, (640, int(image.shape[0] * scale_factor)))

        # Prepare the image for sending to the backend API
        files = {'image': ('image.jpg', cv2.imencode('.jpg', image)[1].tobytes())}

        # Send a POST request to the backend API for people detection
        response = requests.post('http://backend:5000/detect_people', files=files)

        # Extract bounding box information from the JSON response
        bounding_boxes = response.json().get('bounding_boxes', [])

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Draw bounding boxes on the image
            for bbox in bounding_boxes:
                xmin, ymin, xmax, ymax = bbox['xmin'], bbox['ymin'], bbox['xmax'], bbox['ymax']
                confidence = bbox['confidence']
                color = (0, 255, 0)  # Green color
                cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, 2)
                cv2.putText(image, f'{confidence:.2f}', (xmin, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            # Convert the image to base64 for displaying in HTML
            _, buffer = cv2.imencode('.jpg', image)
            image_base64 = base64.b64encode(buffer).decode('utf-8')

            # Render the result page with the annotated image
            return render_template('result.html', image_base64=image_base64)
        else:
            # Render the home page with an error message if processing failed
            return render_template('index.html', message='Error processing image')

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
