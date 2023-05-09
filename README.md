# INTERNSHIP-PYTHON
https://user-images.githubusercontent.com/108046600/236996529-758d2f1f-8195-41ab-bbaa-07a7dbe4ec02.mp4

#code
import numpy as np
import cv2
import os
import pyrebase
import time

firebaseConfig = {
  "apiKey": "AIzaSyD2kcxhZprSwEcLxLbh725VcX7KfHARIbw",
  "authDomain": "mainpro2-8407d.firebaseapp.com",
"databaseURL": "https://mainpro2-8407d-default-rtdb.firebaseio.com/",

  "projectId": "mainpro2-8407d",
  "storageBucket": "mainpro2-8407d.appspot.com",
  "messagingSenderId": "767424569688",
  "appId": "1:767424569688:web:1ef0a6621cb13a465fc52d",
  "measurementId": "G-ST6M8Y1SQY"
};
# const firebaseConfig = {
#   apiKey: "AIzaSyD2kcxhZprSwEcLxLbh725VcX7KfHARIbw",2

#   authDomain: "mainpro2-8407d.firebaseapp.com",
#   projectId: "mainpro2-8407d",
#   storageBucket: "mainpro2-8407d.appspot.com",
#   messagingSenderId: "767424569688",
#   appId: "1:767424569688:web:1ef0a6621cb13a465fc52d",
#   measurementId: "G-ST6M8Y1SQY"
# };
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
# Check if folder exists
if not os.path.exists('images'):
    os.makedirs('images')

faceCascade = cv2.CascadeClassifier(r'C:\Users\ANVITH K\PycharmProjects\pythonProject2\haarcascade_frontalface default.xml');
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
count = 0

face_detector = cv2.CascadeClassifier(r'C:\Users\ANVITH K\PycharmProjects\pythonProject2\haarcascade_frontalface default.xml');

# For each person, enter one unique numeric face id
face_id = input('\n enter user id (MUST be an integer) and press <return> -->  ')
print("\n  Initializing face capture. Look the camera and wait ...")


while(True):
    ret, img = cam.read()
    print(img);
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),2)
        count += 1
        # Save the captured image into the images directory
        cv2.imwrite("./images/Users." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)
    # Press Escape to end the program.
    k = cv2.waitKey(100) & 0xff
    if k < 30:
        break
    # Take 30 face samples and stop video. You may increase or decrease the number of
    # images. The more the better while training the model.
    elif count >= 30:
         break

print("\n [INFO] Exiting Program.")
cam.release()
cv2.destroyAllWindows()

 # detection code completed


import cv2
import numpy as np
from PIL import Image
import os

password=input("enter the password")
#Directory path name where the face images are stored.
path = './images/'
recognizer = cv2.face.LBPHFaceRecognizer_create();
#Haar cascade file
detector =cv2.CascadeClassifier(r'C:\Users\ANVITH K\PycharmProjects\pythonProject2\haarcascade_frontalface default.xml');

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    print(imagePaths)
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        # convert it to grayscale
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img,'uint8')
        id  = int(os.path.split(imagePath)[-1].split('.')[1])
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids
print ("\n[INFO] Training faces...")
faces,ids = getImagesAndLabels(path);
recognizer.train(faces, np.array(ids))
# Save the model into the current directory.
recognizer.write('data.yml')
print("\n[INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))


print("Keep your items")
time.sleep(3)
db.update(data={"on": 0 , "return": 0 ,"face":1 })
# face training completed
import cv2

import numpy as np
import os
import serial
import time
com_port='COM4'
serial = serial.Serial(port=None, baudrate=9600)
headers = {
 'cache-control': "no-cache"
}
def isSecondTime(id,detectedPersonsList):
 if id in detectedPersonsList:
  print("Second Visit..")
  return True
 else:
  return False
def startDevice():
 db.update(data={"on": 1 , "return": 1})
 print('TAke your Luggage!')
 time.sleep(4)
 serial.write(B'1')
 print('device started')
 time.sleep(4)
 serial.write(B'0')
 print('device stoped')
def reverseDevice():
 serial.write(B'2')
 print('device reversed')
 time.sleep(4)
 serial.write(B'0')
 print('device stoped')


faceDetect=cv2.CascadeClassifier(r'C:\Users\ANVITH K\PycharmProjects\pythonProject2\haarcascade_frontalface default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('data.yml')
id=0

# face_cascade_Path =r'C:\Users\ANVITH K\PycharmProjects\pythonProject2\haarcascade_frontalface default.xml'
#
# faceCascade = cv2.CascadeClassifier(face_cascade_Path)

font = cv2.FONT_HERSHEY_SIMPLEX
fontsize=1
fontcolor=(0,511,1)
count=0
Person1Count, Person2Count, Person3Count= 0, 0, 0
c=0
detectedPersonsList=[]
detectedPerson=''
returnedPersonList=[]


# # names related to ids: The names associated to the ids: 1 for Mohamed, 2 for Jack, etc...
# names = ['None','anusha','ananya','nisarga'] # add a name into this list
# #Video Capture
pw=input("enter the password")
if password==pw:
    cam = cv2.VideoCapture(0)
else:
    print("Check your password")
# cam.set(3, 640)
# cam.set(4, 480)
# # Min Height and Width for the  window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)
while True:
    time.sleep(1)
    ret, img = cam.read();

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceDetect.detectMultiScale(
        gray,

        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,180),2)
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        print('detect id:')
        print(id)
        print(confidence);

        if (id==2 and confidence < 50):
            id = "Person1"
            Person1Count= Person1Count + 1

            if Person1Count > 10:
                print('COUNT')
                print(Person1Count)
                if not isSecondTime(id, detectedPersonsList):
                    detectedPersonsList.append(id)
                    startDevice()
                    time.sleep(1)


                else:
                    reverseDevice()
                    time.sleep(1)
                    returnedPersonList.append(id)
                Person1Count = 0


            # confidence = "  {0}%".format(round(100 - confidence))
        else:
            # Unknown Face
            id = "Who are you ?"
        if id in returnedPersonList:
            cv2.putText(img, 'Not Found', (x, y + h + 25), font, fontsize, fontcolor, 2)
        else:
            cv2.putText(img, str(id), (x, y + h + 25), font, fontsize, fontcolor, 2)
        print(id)


    cv2.imshow('Face', img);
    # Escape to exit the webcam / program

    if (cv2.waitKey(1) == ord('q')):
        break
cam.release(50)
cv2.destroyAllWindows()
