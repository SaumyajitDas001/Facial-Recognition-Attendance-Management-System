from tkinter import *
from tkinter import ttk
from typing import Any
from unittest.mock import right
from PIL import Image, ImageTk
from PIL.ImageOps import grayscale
from matplotlib.pyplot import title
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data")

        title_label = Label(self.root, text="Train Data Set", font=("times new roman", 35 , "bold"), bg="blue",fg="yellow")
        title_label.place(x=0,y=0,width=1530,height=45)

        imgtop = Image.open("Face Recognition/facialrecognition.png")
        imgtop = imgtop.resize((1530, 325), Image.LANCZOS)
        self.photoimgtop = ImageTk.PhotoImage(imgtop)

        f_lbl = Label(self.root, image=self.photoimgtop)
        f_lbl.place(x=0, y= 45, width=1530, height=325)

        b = Button(self.root,text="Train Data",command=self.trainclassifier,cursor="hand2",font=("times new roman", 30 , "bold"), bg="Yellow",fg="Red")
        b.place(x=0, y=370, width=1530, height=65)

        imgbottom = Image.open("Face Recognition/facial_recognition_action.jpg")
        imgbottom = imgbottom.resize((1530, 400), Image.LANCZOS)
        self.photoimgbottom = ImageTk.PhotoImage(imgbottom)

        f_lbl = Label(self.root, image=self.photoimgbottom)
        f_lbl.place(x=0, y=440, width=1530, height=400)

    def trainclassifier(self):
        data_dir=("data")
        path=[os.path .join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            if cv2.waitKey(1)==13:
                break
        ids=-np.array(ids)

        #======================Train the classifier=====================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","!!!Training Datasets Completed!!!")







if __name__ == "__main__":
    root=Tk()
    obj = Train(root)
    root.mainloop()