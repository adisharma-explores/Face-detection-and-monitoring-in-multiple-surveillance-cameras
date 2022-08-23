from cv2 import add
import threading
import face_recognition
import cv2
import numpy as np
from functools import partial

from multiprocessing import Pool
import time
from multiprocessing import Process
from check import *

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:

#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
def facerec1(known_face_encodings,address):
    video1=cv2.VideoCapture(1)

   # address="http://192.168.29.90:8080/video"
    video1.open(address)

    print("hi2"+address)
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    flag1=1
    
    while True:
        # Grab a single frame of video
        ret, frame = video1.read()
        
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (224, 224), fx=0, fy=0)
        print("hi22"+address)
        
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            flag1=0
            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                print("hi222"+address)

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    with open('log.txt', 'w') as f:
                        f.write(address)
                    #pool.terminate()
                    # Display the resulting image
                    #cv2.imshow('Video', frame)
        with open('log.txt') as f:
            lines = f.readlines()
        if len(lines)>0:
            break
        process_this_frame = not process_this_frame   
    video1.release()
    #
    # cv2.destroyAllWindows()


        # Display the results


def start1(lis,known_face_encodings1):
    known_face_encodings=known_face_encodings1
    pool = Pool()
    fun=partial(facerec1,known_face_encodings1)                         # Create a multiprocessing Pool
    pool.map(fun, lis)
    print("Result")