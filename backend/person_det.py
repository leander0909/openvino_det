from flask import Flask, request, jsonify
from openvino.inference_engine import IECore
import cv2
import numpy as np

app = Flask(__name__)

# Load the Inference Engine
ie = IECore()

# Load the optimized model (IR files)
model_xml = 'backend/model/pedestrian-detection-adas-0002.xml'
model_bin = 'backend/model/pedestrian-detection-adas-0002.bin'
net = ie.read_network(model=model_xml, weights=model_bin)

# Get the input blob name
input_blob = next(iter(net.input_info))

# Load the network to the Inference Engine
exec_net = ie.load_network(network=net, device_name='CPU')


@app.route('/detect_people', methods=['POST'])
def detect_people():
    try:
        # Get the input image from the frontend
        input_image = request.files['image'].read()

        # Convert bytes to numpy array
        nparr = np.frombuffer(input_image, np.uint8)
        input_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Resize the input image to match the expected input shape of the model
        input_image_resized = cv2.resize(input_image, (672, 384))
        input_image_resized = input_image_resized.transpose((2, 0, 1))
        input_image_resized = input_image_resized.reshape((1, 3, 384, 672))

        # Perform inference
        result = exec_net.infer(inputs={input_blob: input_image_resized})

        # Assuming you have identified the correct output blob name
        output_blob_name = 'detection_out'
        output_image = result[output_blob_name]

        # Process bounding boxes
        bounding_boxes = []
        for detection in output_image[0][0]:
            confidence = detection[2]

            # Adjust the confidence threshold as needed or remove it for all detections
            if confidence > 0.8:  # Adjust the confidence threshold here
                xmin = int(detection[3] * input_image.shape[1])
                ymin = int(detection[4] * input_image.shape[0])
                xmax = int(detection[5] * input_image.shape[1])
                ymax = int(detection[6] * input_image.shape[0])

                bounding_boxes.append({
                    'xmin': xmin,
                    'ymin': ymin,
                    'xmax': xmax,
                    'ymax': ymax,
                    'confidence': float(confidence)  # Convert to regular float
                })

        # Return bounding box information to the frontend
        return jsonify({"result": "success", "bounding_boxes": bounding_boxes})

    except Exception as e:
        return jsonify({"result": "error", "message": str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
