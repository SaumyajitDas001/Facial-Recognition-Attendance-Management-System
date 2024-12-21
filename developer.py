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

class developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_label = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="blue",
                            fg="yellow")
        title_label.place(x=0, y=0, width=1580, height=45)

        imgtop = Image.open("Face Recognition/dev.jpg")
        imgtop = imgtop.resize((1580, 900), Image.LANCZOS)
        self.photoimgtop = ImageTk.PhotoImage(imgtop)

        f_lbl = Label(self.root, image=self.photoimgtop)
        f_lbl.place(x=0, y=45, width=1530, height=900)

        #frame
        frame=Frame(f_lbl,bd=2,bg="light blue")
        frame.place(x=100,y=0,width=1300,height=750)

        img = Image.open("Face Recognition/Saumyajit.jpg")
        img = img.resize((200, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(frame ,image=self.photoimg)
        f_lbl.place(x=1050, y=0, width=200, height=200)

        img1 = Image.open("Face Recognition/sunanda.jpg")
        img1 = img1.resize((200, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(frame, image=self.photoimg1)
        f_lbl.place(x=1050, y=250, width=200, height=200)

        img2 = Image.open("Face Recognition/Rig.jpg")
        img2 = img2.resize((200, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(frame, image=self.photoimg2)
        f_lbl.place(x=1050, y=500, width=200, height=200)

        img3 = Image.open("Face Recognition/sania.jpg")
        img3 = img3.resize((200, 200), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(frame, image=self.photoimg3)
        f_lbl.place(x=750, y=150, width=200, height=200)

        img4 = Image.open("Face Recognition/Sreyan.jpg")
        img4 = img4.resize((200, 200), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        f_lbl = Label(frame, image=self.photoimg4)
        f_lbl.place(x=750, y=450, width=200, height=200)

        # Developer
        dep_label = Label(frame, text="Here are the Team members: \n Saumyajit Das \n Sunanda Patra \n Rig Ghosh \nSania Khandakar \n Sreyan Datta \n who are mentored by Professor Dr. Anirban Ganguly. ", font=("times new roman", 20, "bold"), bg="aquamarine")
        dep_label.place(x=50, y=70)
        dep_label1 = Label(frame,
                          text="!!Thank You For the Guidance!!",
                          font=("times new roman", 30, "bold"), fg="red")
        dep_label1.place(x=80, y=550)
if __name__ == "__main__":
    root = Tk()
    obj = developer(root)
    root.mainloop()