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

class help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Desk")

        title_label = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="aquamarine",
                            fg="purple")
        title_label.place(x=0, y=0, width=1580, height=45)

        imgtop = Image.open("Face Recognition/di.jpg")
        imgtop = imgtop.resize((1580, 850), Image.LANCZOS)
        self.photoimgtop = ImageTk.PhotoImage(imgtop)

        f_lbl = Label(self.root, image=self.photoimgtop)
        f_lbl.place(x=0, y=45, width=1580, height=850)

        dev_label=Label(f_lbl,text="Email: saumyajitdas756@gmail.com \n Phone No: 8910527521",font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=570,y=200)



if __name__ == "__main__":
    root = Tk()
    obj = help(root)
    root.mainloop()