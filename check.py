from cv2 import add
import threading
import face_recognition
import cv2
import numpy as np
import time
from concurrent.futures import thread
from multiprocessing import Pool
import time
from multiprocessing import Process

def facerec2(address):
    obama_image = face_recognition.load_image_file("obama.jpg")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
            # Load a second sample picture and learn how to recognize it.
    biden_image = face_recognition.load_image_file("biden11.jpg")
    biden_image = face_recognition.load_image_file("biden2.jpg")
    biden_image = face_recognition.load_image_file("biden2.jpg")
    print("hi11")
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

            # Create arrays of known face encodings and their names
    known_face_encodings = [
        obama_face_encoding,
        biden_face_encoding
        ]
    known_face_names = [
        "Barack Obama",
        "Joe Biden"
        ]
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
    w=0

    while True:
        # Grab a single frame of video
        ret, frame = video1.read()
        
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
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
                    w=0
                    with open('log.txt', 'w') as f:
                        f.write(address)
                    name = known_face_names[best_match_index]
                    face_names.append(name)
                    for (top, right, bottom, left), name in zip(face_locations, face_names):
                        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                        top *= 4
                        right *= 4
                        bottom *= 4
                        left *= 4

                        # Draw a box around the face
                        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                        # Draw a label with a name below the face
                        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                        font = cv2.FONT_HERSHEY_DUPLEX
                        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

                    # Display the resulting image
                    cv2.imshow('Video', frame)
                else:
                    f = open('log.txt', 'r+')
                    f.truncate(0)
                    cv2.destroyAllWindows()
                    # Hit 'q' on the keyboard to quit!
            if len(face_encodings)==0:
                f = open('log.txt', 'r+')
                f.truncate(0)
                cv2.destroyAllWindows()
        with open('log.txt') as f:
            lines1 = f.readlines()
        print("before w")
        if len(lines1)==0:
            w=w+1
            print(w)
        if w>150:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        process_this_frame = not process_this_frame 
    print(w)  
    video1.release()
    cv2.destroyAllWindows()   



        # Display the results
