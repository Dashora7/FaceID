import cv2
import time
import numpy as np

def train_background(frames):
    cap = cv2.VideoCapture(0)
    flist = []

    for i in range(frames):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        grab, frame = cap.read()
        flist.append(frame)
    med = np.median(flist, axis=0).astype(np.uint8)
    med = cv2.cvtColor(med, cv2.COLOR_BGR2GRAY)
    return med

def begin_motion_alerting(bg, alert_th=0.1):
    cap = cv2.VideoCapture(0)
    ig = False
    c = 0
    while 1:
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(frame, bg)
        th, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
        #ccv2.imshow('frames', diff)
        frac = np.count_nonzero(diff) / (diff.shape[0]*diff.shape[1])
        if frac > alert_th and ig:
            print('motion alert')
            return True
            # TRIGGER BURST CAPTURE FOR LIVENESS AND FACE ID CHECK
            # GET FACE ID PREDICTIONS FROM REALTIME CODE THEN FEED TO LIVENESS MODEL
        c += 1
        if c > 10:
            ig = True
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break


if __name__ == '__main__':
    b = train_background(50)
    begin_motion_alerting(b)