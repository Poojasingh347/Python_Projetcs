from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("13500x700+0+0")
        self.root.configure(bg="dark blue")
        title=Label(self.root,text="Student Management System",bd=8,relief=GROOVE,font=("Verdana 10 bold",40,"bold"),bg="grey",fg="dark blue")
        title.pack(side=TOP,fill=X)


        #===========All Variable===============
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        #============Manage Frame==============
         
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        M_title=Label(Manage_Frame,bg="crimson",fg="white",text="Manage Students",font=("Veradana 10 bold",20,"bold"))
        M_title.grid(row=0,columnspan=2,pady=10)

        #ROLL NO
        
        Roll_No=Label(Manage_Frame,bg="crimson",fg="white",text="Roll No.",font=("Verdana 10 bold",15,"bold"))
        Roll_No.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("verdana 10 bold",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        #NAME OF THE STUDENT
        
        Name=Label(Manage_Frame,bg="crimson",fg="white",text="Name",font=("Verdana 10 bold",15,"bold"))
        Name.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Name=Entry( Manage_Frame,textvariable=self.name_var,font=("verdana 10 bold",15,"bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=1,column=1,pady=10,padx=20,sticky="w")


        #EMAIL_ID
        
        Email_Id=Label(Manage_Frame,bg="crimson",fg="white",text="Email",font=("Verdana 10 bold",15,"bold"))
        Email_Id.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_Email_id=Entry( Manage_Frame,textvariable=self.email_var,font=("verdana 10 bold",15,"bold"),bd=5,relief=GROOVE)
        txt_Email_id.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        #GENDER
        
        Gender=Label(Manage_Frame,bg="crimson",fg="white",text="Gender",font=("Verdana 10 bold",15,"bold"))
        Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        Combo_Gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("Verdana 10 bold",14,"bold"),state="readonly")
        Combo_Gender['values']=('Male','Female','Others')
        Combo_Gender.grid(row=4,column=1,pady=10,padx=20)

        #CONTACT
        Contact_No=Label(Manage_Frame,bg="crimson",fg="white",text="Contact No",font=("Verdana 10 bold",15,"bold"))
        Contact_No.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_Contact_No=Entry( Manage_Frame,textvariable=self.contact_var,font=("verdana 10 bold",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact_No.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        #D.O.B
        D_O_B=Label(Manage_Frame,bg="crimson",fg="white",text="D.O.B",font=("Verdana 10 bold",15,"bold"))
        D_O_B.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_D_O_B=Entry(Manage_Frame,textvariable=self.dob_var,font=("verdana 10 bold",15,"bold"),bd=5,relief=GROOVE)
        txt_D_O_B.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        #ADDRESS
        Address=Label(Manage_Frame,bg="crimson",fg="white",text="Address",font=("Verdana 10 bold",15,"bold"))
        Address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_Address=Text(Manage_Frame,width="32",height=4,font=("",10))
        self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        #========Button========
        btn_Frame=Frame(Manage_Frame,bd=4,relief=GROOVE,bg="crimson")
        btn_Frame.place(x=10,y=500,width=430)

        Addbtn=Button(btn_Frame,text="Add",bg="grey",fg="white",width=8,height=2,font=("Verdana 10 bold"),command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn=Button(btn_Frame,text="Update",bg="grey",fg="white",width=8,padx=2,height=2,font=("Verdana 10 bold"),command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn=Button(btn_Frame,text="Delete",bg="grey",fg="white",width=8,padx=2,height=2,font=("Verdana 10 bold"),command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",bg="grey",fg="white",width=8,padx=2,height=2,font=("Verdana 10 bold"),command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        
        #============Detailed Frame============
         
        Detailed_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detailed_Frame.place(x=550,y=100,width=785,height=575)

        lbl_Search=Label(Detailed_Frame,bg="crimson",fg="white",text="Search By",font=("Verdana 10 bold",20,"bold"))
        lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")


        Combo_Search=ttk.Combobox(Detailed_Frame,textvariable=self.search_by,font=("Verdana 10 bold",10,"bold"),state="readonly")
        Combo_Search['values']=('Roll_no','Name','Contact')
        Combo_Search.grid(row=0,column=1,pady=10,padx=20)

        txt_Search=Entry(Detailed_Frame,textvariable=self.search_txt,width=20,font=("Verdana 10 bold",10,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        Search_btn=Button(Detailed_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        Showall_btn=Button(Detailed_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)


        #=========TABLE FRAME===============
        Table_Frame=Frame(Detailed_Frame,bd=4,relief=RIDGE,bg="Crimson")
        Table_Frame.place(x=10,y=70,width=760,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,column=("roll","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll no")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact No")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("Address",width=100)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="" or self.txt_Address.get('1.0',END)=="":
            messagebox.showerror("Error","All Fields are required")
        else:
            
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                         self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.txt_Address.get('1.0',END)
                                                                         ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])

    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                         self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.txt_Address.get('1.0',END),
                                                                         self.Roll_No_var.get()
                                                                         ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    
    
root=Tk()
obj=Student(root)
root.mainloop()
