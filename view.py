import cv2
import zmq
import base64
import numpy as np
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 6060))
n = 500
t0 = time.time()

for i in range(n):
    try:
        msg = s.recv(20000)
        img = base64.b64decode(msg)
        source = np.frombuffer(img, dtype=np.uint8)
        #source = cv2.imdecode(npimg, 1)
        #print('received')
        cv2.imshow("Stream", source)
        cv2.waitKey(1)
        
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        break

framerate = n/(time.time() - t0)
print(str(framerate))
"""
context = zmq.Context()
footage_socket = context.socket(zmq.SUB)
footage_socket.bind('tcp://*:9090')
footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
n = 500
t0 = time.time()
for i in range(n):
    try:
        frame = footage_socket.recv_string()
        img = base64.b64decode(frame)
        npimg = np.frombuffer(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        cv2.imshow("Stream", source)
        cv2.waitKey(1)

    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        break

framerate = n/(time.time() - t0)
print(str(framerate))
"""