# opencv_det
## Dockerized website for human detection, using Python, Flask and OpenCV

### **First thing to do is clone this repository:**

``` git clone https://github.com/leander0909/opencv_det.git ``` </br>
**Your folder hierarcy should look like this:**

```
openvino_det/
|
├── docker-compose.yml
├── backend/
|   ├── Dockerfile
|   ├── person_det.py
|   ├── requirements.txt
│   └── model/
│       ├── pedestrian-detection-adas-0002.bin
|       └── pedestrian-detection-adas-0002.xml
└── frontend/
    ├── Dockerfile
    ├── frontend.py
    ├── requirements.txt
    └── templates/
        ├── index.html
        └── result.html
```
### Second is you need to install ```Docker```, the easiest way will be installing Docker Desktop in which I used. You can follow this tutorial here in the video below:

[![DOCKER Installation Tutorial](https://img.youtube.com/vi/XgRGI0Pw2mM&t/0.jpg)](https://www.youtube.com/watch?v=XgRGI0Pw2mM&t=47s)

You have different Docker containers for frontend and backend. Docker is necessary so that you can separate different dependencies to prevent "dependency conflict" or "dependency collision".

### Once you make your Docker up and running (necessary for running the whole website), you can go to your terminal at your root directory which is ```openvino_det```, then run the code below:

``` docker-compose up --build ```

The code above will setup the two Docker containers, one for frontend and one for backend. The code will install the necessary dependencies needed for each container.

Now you can visit ``` http://127.0.0.1:80 ``` on your local browser to access the website.




## Here is the flow of the whole code:
```Frontend (frontend/frontend.py):```
1. Frontend: <br />
    - The frontend is a Flask web application that serves an HTML template at the root route ("/")
2. Upload Page (/upload): <br />
  *User uploads an image through a form. <br />
  *The image is sent as a POST request to /upload route.
3. Image Upload Handling: <br />
  *The Flask app in the frontend (frontend.py) prepares the image data. <br />
  *Sends a POST request to the OpenCV backend (detect_people endpoint) with the image attached.




```Backend (opencv_backend/detect_people.py):``` <br />
1. Detect People Endpoint (/detect_people): <br />
  *Listens for POST requests containing an image to process.
2. Image Processing: <br />
  *Retrieves the image from the POST request. <br />
  *Converts the image from bytes to a NumPy array using OpenCV. <br />
  *Converts the image to grayscale.
3. HOG Descriptor and Detection: <br />
  *Initializes a Histogram of Oriented Gradients (HOG) descriptor. <br />
  *Sets the Support Vector Machine (SVM) detector for detecting people. <br />
  *Detects people in the image using HOG.
4. Drawing Bounding Boxes: <br />
  *Draws bounding boxes around detected people in the image.
5. Image Encoding and Base64 Conversion: <br />
  *Encodes the processed image to JPEG format. <br />
  *Converts the encoded image to base64.
6. JSON Response: <br />
  *Sends a JSON response containing the base64-encoded image data.


```Frontend (frontend/frontend.py):``` <br />
1. Image Processing Response: <br />
  *Waits for the response from the backend. <br />
  *Attempts to parse the JSON response from the backend.
2. Result Page (/result): <br />
  *Renders a result page (result.html) with the processed image received from the backend. <br />
3. Result Rendering: <br />
  *Renders the result page (result.html) with the processed image data received from the backend. <br />
  *The processed image is displayed on the result page. <br />

   

```Overall Flow:``` <br />
  *User uploads an image on the frontend. <br />
  *The image is sent to the OpenCV backend for people detection. <br />
  *The backend processes the image, detects people, and sends back the result. <br />
  *The frontend renders a result page displaying the original and processed images.
