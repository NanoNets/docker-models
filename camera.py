import requests
import cv2
import json


url = 'http://localhost:5000/'

#-----GET CAMERA FEED----
cap = cv2.VideoCapture(0)

# Check if the drone feed is opened correctly
if not cap.isOpened():
    raise IOError("Cannot connect to drone feed.")

ret, frame = cap.read()
height, width, _ = frame.shape

while True:
    #-----GET WEBCAM FRAME----
    ret, frame = cap.read()


    #-----DO SOMETHING-----

    _, img_encoded = cv2.imencode('.jpg', frame)
    response = requests.post(
        url, auth=requests.auth.HTTPBasicAuth('YOUR_API_KEY', ''),
        files={"file": ("frame.jpg", img_encoded.tostring())},
    )
    response = json.loads(response.text)
    
    prediction = response[0]["prediction"]
    for i in prediction:
        frame = cv2.rectangle(frame,(i['xmin'],i['ymin']),(i['xmax'],i['ymax']),(0,0,255),2)

    #-----END OF DO SOMETHING-----

    
    cv2.imshow('bird', frame)
    
    # Press esc to exit/stop
    c = cv2.waitKey(1)
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)