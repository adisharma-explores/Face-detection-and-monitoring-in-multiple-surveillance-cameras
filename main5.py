import os
from concurrent.futures import thread
from multiprocessing import Pool
from check2 import *
from test17 import *
from dahboard import*
from loginscreen import *
from name import *
from design1 import *
from ipinput import *
flag=0
if __name__=="__main__":
    login()
    t=upload_file()
    name=nam()
    print(name)
    [a,b]=ipadda()
    print(a)
    print(b)
    flag=1
    known_face_encodings = []
    #for i in range(0,len(t)):
    obama_image = face_recognition.load_image_file(t[0])
    known_face_encodings.append(face_recognition.face_encodings(obama_image)[0])
    print(known_face_encodings)
    known_face_names = [
        name
        ]
    i=0
    p2=[]
    #a=["http://192.168.84.137:8080/video","http://192.168.84.32:8080/video","http://192.168.84.28:8080/video"]
   # b=[[2,3],[1],[1]]
    start1(a,known_face_encodings)
    while(True):
        with open('log.txt') as f:
            lines = f.readlines()
        print(lines)
        if len(lines)>0:
            cam=lines[0]
            index1=a.index(cam)
            index1=index1+1
            s="Detected in room "+str(index1)
            with open('log1.txt', 'a') as f:
                f.write(s+",\n")
            logg()
            facerec3(cam,known_face_encodings,known_face_names)
            cam=lines[0]
        else:
            index=a.index(cam)
            lis=b[index]
            cams=[]
            for l in lis:
                l1=int(l)
                cams.append(a[l1-1])
            cams.append(cam)
            start1(cams,known_face_encodings)