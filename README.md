# FaceID
A Face identification and streaming system for a lock

This repo will allow you to live stream and run facial recognition.

You must first fill the "people" directory with images of just your face and name the folder after your name. Then, run the make align data to take these pictures
and crop them to inlcude just a face.

Next, after you have a directory of aligned images, you can call make classifier to take this data, calculate features, and save a model for classifying the different
people that were aligned.

Lastly, you can run realtime facenet to utilize the classifier you trained along with the FaceNet model to continuously crop, embed, and classify frames directly from
a stream.

There is a model for detecting liveness to prevent spoofing (i.e.showing a photo of someone to the camera).

I have some of my own images and alignments as an example
