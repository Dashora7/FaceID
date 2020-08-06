import base64
import cv2
import zmq
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6060))
s.listen()
clientsocket, address = s.accept()
print(address)
camera = cv2.VideoCapture(0)
#camera.set(cv2.CAP_PROP_FPS, 10)
while True:
    try:
        grabbed, frame = camera.read()  # grab the current frame
        #frame = cv2.resize(frame, (640, 480))  # resize the frame
        
        
        cv2.imwrite("img.jpg", frame)
        with open("img.jpg", 'rb') as f:
            jpg_as_text = base64.b64encode(f.read())
        
        
        
        
        '''
        encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 30])
        jpg_as_text = base64.b64encode(buffer)
        '''
    
        clientsocket.send(jpg_as_text)
        
    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        break



"""
context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.connect('tcp://localhost:9090')

camera = cv2.VideoCapture(1)  # init the camera
while True:
    try:
        grabbed, frame = camera.read()  # grab the current frame
        frame = cv2.resize(frame, (640, 480))  # resize the frame
        
        encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 30])
        jpg_as_text = base64.b64encode(buffer)
        
        '''
        cv2.imwrite("img.jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
        with open("img.jpg", 'rb') as f:
            jpg_as_text = base64.b64encode(f.read())
        '''
        footage_socket.send(jpg_as_text)

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        break
"""