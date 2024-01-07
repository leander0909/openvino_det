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

