# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:19:33 2020

@author: nrdas
"""

# import required libraries
from vidgear.gears import NetGear
import cv2

options = {'secure_mode': 1, 'compression_param':cv2.IMREAD_UNCHANGED}
#define Netgear Client with `receive_mode = True` and default parameter
client = NetGear(pattern = 1, receive_mode = True, logging = True, **options)

# loop over
while True:

    # receive frames from network
    frame = client.recv()

    # check for received frame if Nonetype
    if frame is None:
        break


    # {do something with the frame here}


    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close client
client.close()