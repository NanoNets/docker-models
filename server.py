from flask import Flask,request,jsonify
import tensorflow as tf
import numpy as np
import json
import cv2
import os

app = Flask(__name__)

importPath = app.root_path

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(os.path.join(importPath, 'frozen_inference_graph_face.pb'), 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, -1)).astype(np.uint8)

sess = None
with detection_graph.as_default():
    sess = tf.Session(graph=detection_graph)

@app.route("/", methods=['GET', 'POST'])
def hello():
            # Definite input and output Tensors for detection_graph
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            # Each box represents a part of the image where a particular object was detected.
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            # Each score represent how level of confidence for each of the objects.
            # Score is shown on the result image, together with the class label.
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            localizationOuts = []
            file = request.files['file']
            #file.save(os.path.join(importPath, file.filename))
            #images_path = [os.path.join(importPath, file.filename)]
            img_data=file.read()
            #print img_data
            #for image_path in images_path:
            localizationOut = {}
            localizationOut["input"] = file.filename
            
            ### to solve the issue on prediction on one chanel or four channel image.
            ### convert('RGB') will force image to be 3-chanel
            
            #image = Image.open(os.path.join(importPath, image_path)).convert('RGB')
            # the array based representation of the image will be used later in order to prepare the
            # result image with boxes and labels on it.
            #image_np = load_image_into_numpy_array(image)
            image_np = cv2.imdecode(np.fromstring(img_data, dtype=np.uint8), -1)
            # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
            image_np_expanded = np.expand_dims(image_np, axis=0)
            # Actual detection.
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: image_np_expanded})

            localizationBoxes = []
            for i in range(num):
                if scores[0, i] > 0.5:
                    localizationBox = {}
                    localizationBox["label"] = str('foobar')
                    localizationBox["ymin"] = int(boxes[0, i, 0]*image_np.shape[0])
                    localizationBox["xmin"] = int(boxes[0, i, 1]*image_np.shape[1])
                    localizationBox["ymax"] = int(boxes[0, i, 2]*image_np.shape[0])
                    localizationBox["xmax"] = int(boxes[0, i, 3]*image_np.shape[1])
                    localizationBox["score"] = float(scores[0, i])

                    localizationBoxes.append(localizationBox)


            localizationOut["prediction"] = localizationBoxes
            localizationOuts.append(localizationOut)

            return json.dumps(localizationOuts)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')