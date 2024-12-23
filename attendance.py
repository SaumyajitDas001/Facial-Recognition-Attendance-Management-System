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
import csv
from tkinter import filedialog



mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance")

        #=============variables=============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        # First Image
        img = Image.open("Face Recognition/smart-attendance.jpg")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # Second Image
        img1 = Image.open("Face Recognition/clg.jpg")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        # Bg Image
        img3 = Image.open("Face Recognition/bg.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # label title
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM",
                          font=("times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # main frame
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=7, y=55, width=1510, height=650)

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                font=("Times New Roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=740, height=630)

        img_left = Image.open("Face Recognition/vecteezy_set-of-students-concept-vector_8944569.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=7, y=135, width=720, height =370)
        #Label and Entry
        #attendance ID
        attendaceId_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 13, "bold"), bg="white")
        attendaceId_label.grid(row=0, column=0, padx=10, sticky=W)

        attendaceID_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_id,
                                    font=("times new roman", 13, "bold"))
        attendaceID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # NAME
        rollLabel_label = Label(left_inside_frame, text="ROLL :", font=("times new roman", 13, "bold"),
                                  bg="white")
        rollLabel_label.grid(row=0, column=2, padx=8, sticky=W)

        rollLabel_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_roll,
                                      font=("times new roman", 13, "bold"))
        rollLabel_entry.grid(row=0, column=3, padx=8, sticky=W)

        # date
        nameLabel_label = Label(left_inside_frame, text="NAME:", font=("times new roman", 13, "bold"),
                                  bg="white")
        nameLabel_label.grid(row=1, column=0, padx=10, sticky=W)

        nameLabel_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_name,
                                      font=("times new roman", 13, "bold"))
        nameLabel_entry.grid(row=1, column=1, padx=10, sticky=W)

        # Department
        Department_label = Label(left_inside_frame, text="Department :", font=("times new roman", 13, "bold"),
                                  bg="white")
        Department_label.grid(row=1, column=2, padx=10, sticky=W)

        Department_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_dep,
                                      font=("times new roman", 13, "bold"))
        Department_entry.grid(row=1, column=3, padx=10, sticky=W)

        # time
        time_label = Label(left_inside_frame, text="Time :", font=("times new roman", 13, "bold"),
                                  bg="white")
        time_label.grid(row=2, column=0, padx=10, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_time,
                                      font=("times new roman", 13, "bold"))
        time_entry.grid(row=2, column=1, padx=10, sticky=W)

        # date
        dateLabel_label = Label(left_inside_frame, text="Date:", font=("times new roman", 13, "bold"),
                                  bg="white")
        dateLabel_label.grid(row=2, column=2, padx=10, sticky=W)

        dateLabel_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_date,
                                      font=("times new roman", 13, "bold"))
        dateLabel_entry.grid(row=2, column=3, padx=10, sticky=W)

        # attendance
        attendance_label = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 13, "bold"),
                                  bg="white")
        attendance_label.grid(row=3, column=0, padx=10, sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,font="comicsansns 11 bold" ,textvariable=self.var_atten_attendance, state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)

        save_btn = Button(btn_frame, text="Import CSV.", command=self.importCSV, width=17, font=("times new roman", 13, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export CSV.", command=self.exportCSV, width=17,
                            font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", width=17,
                            font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=17, command=self.reset_data,
                           font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",
                                 font=("Times New Roman", 12, "bold"))
        Right_frame.place(x=760, y=10, width=740, height=630)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=710, height=455)

        #=========Scroll bar=========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #===========face data=============

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #===========export csv=============
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported!! to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")





if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()