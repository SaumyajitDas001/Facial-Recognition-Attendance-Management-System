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



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #==============variable===========
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = IntVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # First Image
        img = Image.open("Face Recognition/face-recognition.png")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second Image
        img1 = Image.open("Face Recognition/smart-attendance.jpg")
        img1 = img1.resize((510, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=501, y=0, width=510, height=130)

        # Third Image
        img2 = Image.open("Face Recognition/aa.jpg")
        img2 = img2.resize((550, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1001, y=0, width=550, height=130)

        # Bg Image
        img3 = Image.open("Face Recognition/bg.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # label title
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 35, "bold"), bg="white", fg="dark red")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        #main frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=7,y=55,width=1510,height=650)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Times New Roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=740,height=630)

        img_left = Image.open("Face Recognition/vecteezy_set-of-students-concept-vector_8944569.jpg")
        img_left = img_left.resize((720,130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        #current course
        course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",
                                font=("Times New Roman", 12, "bold"))
        course_frame.place(x=5, y=135, width=720, height=150)

        # Department
        dep_label=Label(course_frame,text="Department",font=("times new roman", 12, "bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(course_frame,textvariable=self.var_dep,font=("times new roman", 12, "bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Electronics","Mechanical","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course
        course_label=Label(course_frame, text="Course", font=("times new roman", 13, "bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10, sticky=W)

        course_combo= ttk.Combobox(course_frame,textvariable=self.var_course, font=("times new roman", 13, "bold"),
                                    state="readonly",width=20)
        course_combo["values"]=("Select Course", "Btech", "Mtech")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky= W)

        # Year
        year_label = Label(course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(course_frame,textvariable=self.var_year, font=("times new roman", 13, "bold"),
                                    state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-2023", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        Semester_label = Label(course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        Semester_label.grid(row=1, column=2, padx=10, sticky=W)

        Semester_combo = ttk.Combobox(course_frame,textvariable=self.var_semester, font=("times new roman", 13, "bold"),
                                    state="readonly", width=20)
        Semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2","Semester-3","Semester-4")
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        #student Information
        student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",
                                  font=("Times New Roman", 12, "bold"))
        student_frame.place(x=5, y=285, width=720, height=320)

        # student id
        studentId_label = Label(student_frame, text="StudentID:", font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry=ttk.Entry(student_frame,textvariable=self.var_std_id,width=20,font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        #student Name
        studentName_label = Label(student_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10,pady=5, sticky=W)

        studentNAME_entry = ttk.Entry(student_frame,textvariable=self.var_std_name, width=20, font=("times new roman", 13, "bold"))
        studentNAME_entry.grid(row=0, column=3, padx=10,pady=5, sticky=W)

        #class division
        classDivision_label = Label(student_frame, text="Class Division:", font=("times new roman", 13, "bold"), bg="white")
        classDivision_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_combo = ttk.Combobox(student_frame, textvariable=self.var_div, font=("times new roman", 13, "bold"),
                                    state="readonly", width=18)
        div_combo["values"] = ("A", "B", "C", "D", "E","F","G", "H", "I", "J", "K","L","M", "N", "O")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, sticky=W)

        # roll no
        rol_label = Label(student_frame, text="Roll Number:", font=("times new roman", 13, "bold"), bg="white")
        rol_label.grid(row=1, column=2, padx=10, sticky=W)

        roll_entry = ttk.Entry(student_frame,textvariable=self.var_roll, width=20, font=("times new roman", 13, "bold"))
        roll_entry.grid(row=1, column=3, padx=10, sticky=W)

        # gender
        Gender_label = Label(student_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        Gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(student_frame, textvariable=self.var_gender, font=("times new roman", 13, "bold"),
                                  state="readonly", width=18)
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, sticky=W)

        # DOB
        DOB_label = Label(student_frame, text="Date Of Birth:", font=("times new roman", 13, "bold"),
                                    bg="white")
        DOB_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        Dob_entry = ttk.Entry(student_frame,textvariable=self.var_dob, width=20, font=("times new roman", 13, "bold"))
        Dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(student_frame, text="Email:", font=("times new roman", 13, "bold"),
                                    bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(student_frame,textvariable=self.var_email, width=20, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone number
        phone_label = Label(student_frame, text="Phone Number:", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, sticky=W)

        phone_entry = ttk.Entry(student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, sticky=W)

        # Address
        address_label = Label(student_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(student_frame,textvariable=self.var_address, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher's Name
        teacher_label = Label(student_frame, text="Teacher:", font=("times new roman", 13, "bold"),
                          bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(student_frame,textvariable=self.var_teacher, width=20, font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio Buttons
        self.var_radio1 = StringVar()
        radionbtn1 = ttk.Radiobutton(student_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radionbtn1.grid(row=6, column=0)
        radionbtn2 = ttk.Radiobutton(student_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radionbtn2.grid(row=6, column=1)

        # buttons frame
        btn_frame = Frame(student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=35)

        save_btn=Button(btn_frame, text="Save",command=self.add_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn=Button(btn_frame, text="Update",command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn=Button(btn_frame, text="Delete",command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame, text="Reset",command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # lower button frame
        btn1_frame = Frame(student_frame, bd=2, relief=RIDGE, bg="white")
        btn1_frame.place(x=0, y=235, width=715, height=35)

        lower_btn = Button(btn1_frame,command=self.generate_dataset, text="Take Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue",
                           fg="white")
        lower_btn.grid(row=1, column=0)
        lower1_btn = Button(btn1_frame, text="Update Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue",
                           fg="white")
        lower1_btn.grid(row=1, column=2)


        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("Times New Roman", 12, "bold"))
        Right_frame.place(x=760, y=10, width=740, height=630)

        img_right = Image.open("Face Recognition/sstu.jpg")
        img_right = img_right.resize((720, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

         #========Search System===========
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                   font=("Times New Roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=720, height=70)

        search_label=Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg = "red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=20, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=9, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        showall_btn=Button(search_frame, text="Show All", width=9, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        showall_btn.grid(row=0, column=4,pady=5, sticky=W)

         #==========Table============
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=300)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,  columns=("dep","course","Year","Semester","Student_id","Name","Division","Roll_No","Gender","Date_of_Birth","Email","Phone","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Student_id", text="StudentID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Division", text="Division")
        self.student_table.heading("Roll_No", text="Roll no")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Date_of_Birth", text="Date of Birth")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table.heading("Photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("Student_id", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Division", width=100)
        self.student_table.column("Roll_No", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Date_of_Birth", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Teacher", width=100)
        self.student_table.column("Photo", width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #==============Function==============

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                # Connect to the database
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Saumyajit@2004",
                    database="face_recogniser"
                )
                print("Database connected successfully!")

                # Create a cursor object
                mycursor = conn.cursor()

                # Insert data into the student table
                mycursor.execute(
                    "INSERT INTO student (dep, course, `Year`, Semester, Student_id, Name, `Division`, `Roll_No`, Gender, `Date_of_Birth`, Email, Phone, Address, Teacher, Photo) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get()
                    )
                )

                # Commit the transaction
                conn.commit()
                self.fetch_data()  # Refresh data in the GUI

                # Close the connection
                conn.close()

                # Show success message
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)

            except mysql.connector.Error as db_error:
                # Handle database errors
                messagebox.showerror("Database Error", f"Failed to insert data: {db_error}", parent=self.root)

            except Exception as ex:
                # Handle general exceptions
                messagebox.showerror("Error", f"An unexpected error occurred: {str(ex)}", parent=self.root)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Saumyajit@2004",
                database="face_recogniser"
            )
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM student")
            data = mycursor.fetchall()

            if data:  # Only proceed if there is data
                self.student_table.delete(*self.student_table.get_children())
                for row in data:
                    self.student_table.insert("", END, values=row)
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

     #===========get cursor==============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

#===========update function===========
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                # Ask the user for confirmation before updating
                Update = messagebox.askyesno("Update", "Do You Want to Update Student Details?", parent=self.root)
                if Update:
                    # Connect to the database
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Saumyajit@2004",
                        database="face_recogniser"
                    )
                    mycursor = conn.cursor()
                    update_query = """
                        UPDATE student
                        SET dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, `Roll_No`=%s, Gender=%s,
                        `Date_of_Birth`=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photo=%s
                        WHERE Student_id=%s
                    """
                    mycursor.execute(update_query, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student Details Successfully Updated", parent=self.root)
                else:
                    return

            except mysql.connector.Error as db_error:
                # Handle MySQL database errors
                messagebox.showerror("Database Error", f"Failed to update data: {db_error}", parent=self.root)
                print(f"Database error: {db_error}")

            except Exception as ex:
                # Handle any other exceptions
                messagebox.showerror("Error", f"An unexpected error occurred: {str(ex)}", parent=self.root)
                print(f"Unexpected error: {str(ex)}")

    #delete data
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student?",
                                             parent=self.root)
                if delete:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Saumyajit@2004",
                        database="face_recogniser"
                    )
                    mycursor = conn.cursor()
                    sql = "DELETE FROM student WHERE Student_id=%s"
                    val = (self.var_std_id.get(),)
                    mycursor.execute(sql, val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
                else:
                    return

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    #=========reset===========
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #================== Generate Data Set or take photo samples=================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Saumyajit@2004",
                    database="face_recogniser"
                )
                mycursor = conn.cursor()

                student_id = self.var_std_id.get() if self.var_std_id.get() != "" else None
                roll_no = self.var_roll.get() if self.var_roll.get() != "" else None
                phone = self.var_phone.get() if self.var_phone.get() != "" else None

                # Handle roll_no and phone as numeric values
                if roll_no and not roll_no.isdigit():
                    raise ValueError("Roll Number must be a numeric value.")
                if phone and not phone.isdigit():
                    raise ValueError("Phone number must be a numeric value.")

                mycursor.execute("select * from student")
                myresult = mycursor.fetchall()

                id = 0
                for x in myresult:
                    id += 1

                mycursor.execute(
                    "UPDATE Student SET dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, `Roll_No`=%s, Gender=%s, `Date_of_Birth`=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photo=%s WHERE Student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get() if self.var_year.get() != "" else None,  # Handle empty year field
                        self.var_semester.get() if self.var_semester.get() != "" else None,
                        # Handle empty semester field
                        self.var_std_name.get(),
                        self.var_div.get(),
                        roll_no,
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        phone,
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        student_id==id+1  # Pass the actual student_id here
                    )
                )

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Initialize the face classifier
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor=1.3
                    # Minimum neighbor = 5

                    if len(faces) == 0:
                        return None
                    for (x, y, w, h) in faces:
                        cropped_face = img[y:y + h, x:x + w]
                    return cropped_face

                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, frame = cap.read()
                    if face_cropped(frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(frame), (200, 200))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        # (50,50) is the origin point from where text is to be written
                        # font scale=1
                        # thickness=2

                        cv2.imshow("Cropped face", face)
                        if cv2.waitKey(1) == 13 or int(img_id) == 200:
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Result', 'Generating dataset completed!!!')

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()