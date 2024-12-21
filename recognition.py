from platform import release
from tkinter import *
from tkinter import ttk
from typing import Any
from unittest.mock import right
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
from PIL import features
from PIL.ImageOps import grayscale
from matplotlib.pyplot import title
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Recognize")

        title_label = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), bg="white",
                            fg="green")
        title_label.place(x=0, y=0, width=1530, height=52)

        imgleft = Image.open("Face Recognition/face_detector1.jpg")
        imgleft = imgleft.resize((650, 786), Image.LANCZOS)
        self.photoimgleft = ImageTk.PhotoImage(imgleft)

        f_lbl = Label(self.root, image=self.photoimgleft)
        f_lbl.place(x=0, y=55, width=650, height=786)

        imgright = Image.open("Face Recognition/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        imgright = imgright.resize((950, 786), Image.LANCZOS)
        self.photoimgright = ImageTk.PhotoImage(imgright)

        f_lbl = Label(self.root, image=self.photoimgright)
        f_lbl.place(x=650, y=55, width=950, height=786)

        b = Button(f_lbl, text="Face Recognition",command=self.face, cursor="hand2",
                   font=("times new roman", 18, "bold"), bg="blue", fg="white")
        b.place(x=365, y=692, width=200, height=40)


    #=========================Attendance==========================
    def mark_attendance(self,id,i,j,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((id not in name_list) and (i not in name_list) and (j not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{id},{i},{j},{d},{dtString},{d1},Present")


    #=================face recognition===================
    def face(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coords = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                id, pred = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = max(0, int(100 * (1 - pred / 300)))

                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Saumyajit@2004",
                    database="face_recogniser"
                )
                mycursor = conn.cursor()

                mycursor.execute("SELECT Name FROM student WHERE Student_id = %s", (id,))
                i = mycursor.fetchone()
                i = i[0] if i else "UNKNOWN"

                mycursor.execute("SELECT Roll_No FROM student WHERE Student_id = %s", (id,))
                j = mycursor.fetchone()
                j = j[0] if j else "UNKNOWN"

                mycursor.execute("SELECT dep FROM student WHERE Student_id = %s", (id,))
                d = mycursor.fetchone()
                d = d[0] if d else "UNKNOWN"

                if confidence > 74:
                    cv2.putText(img, "Detected", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
                else:
                    cv2.putText(img, "UNKNOWN", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

                coords = [x, y, w, h]
            return coords

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture = cv2.VideoCapture(0)

        while True:
            ret, img = video_capture.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("face detection", img)

            if cv2.waitKey(1) == 13:  # Enter key to exit
                break

        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj = Recognition(root)
    root.mainloop()