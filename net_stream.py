# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:19:34 2020

@author: nrdas
"""

# import required libraries
from vidgear.gears import VideoGear
from vidgear.gears import NetGear
import cv2
from vidgear.gears import CamGear

# open any valid video stream(for e.g `test.mp4` file)
stream = CamGear(source=0).start()
options = {'secure_mode': 1, 'compression_format': '.jpg', 'compression_param':[cv2.IMWRITE_JPEG_QUALITY, 60]} 
#Define Netgear Server with default parameters
server = NetGear(pattern = 1, logging = True, **options)

# loop over until KeyBoard Interrupted
while True:

  try: 

     # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # {do something with the frame here}

    # send frame to server
    server.send(frame)

  except KeyboardInterrupt:
    break

# safely close video stream
stream.stop()

# safely close server
server.close()