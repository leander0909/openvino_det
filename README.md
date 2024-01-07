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
    - The frontend is a Flask web application that serves an HTML template at the root route ("/") <br />
    - When the user uploads an image through the web interface, the /upload endpoint is triggered. <br />
    - The uploaded image is read and resized if its width is greater than 640 pixels. <br />
    - The resized image is then converted to a byte stream and sent as a file in a POST request to the /detect_people endpoint of the backend. <br />

```Backend (backend/person_det.py):```
2. Backend: <br />
    - The backend is a Flask web application that runs an Inference Engine (OpenVINO) to perform pedestrian detection. <br />
    - The backend loads the pre-trained pedestrian detection model (IR files) using OpenVINO. <br />
    - It defines an endpoint /detect_people that accepts POST requests with an image file. <br />
    - Upon receiving the image file, it converts the image from bytes to a NumPy array using OpenCV. <br />
    - The input image is resized to match the expected input shape of the model (672x384 pixels). <br />
    - Inference is performed on the resized image using the loaded model through the Inference Engine. <br />
    - The bounding boxes of detected pedestrians are extracted based on a confidence threshold (set at 0.8 in this case). <br />
    - The bounding box information, including coordinates and confidence scores, is then sent back to the frontend as a JSON response. <br />

```Frontend (frontend/frontend.py):```
3. Frontend: (Continued) <br />
    - The frontend receives the JSON response from the backend containing bounding box information.
    - If the response status code is 200 (indicating success), the frontend draws bounding boxes on the original image using OpenCV.
    - The image with bounding boxes is then converted to base64 encoding for display in HTML.
    - The frontend renders the result.html template, displaying the processed image with bounding boxes and confidence scores.
   

```Overall Flow:``` <br />
  *User uploads an image on the frontend. <br />
  *The image is sent to the OpenCV backend for people detection. <br />
  *The backend processes the image, detects people, and sends back the result. <br />
  *The frontend renders a result page displaying the original and processed images.
