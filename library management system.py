from tkinter import *
from tkinter import ttk
#import mysql.connector
from tkinter import messagebox
import datetime

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1366x768+0+0")

        # Variable declarations
        self.member_var = StringVar()
        self.prnno_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.days_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finallprice_var = StringVar()
        self.id_var=StringVar()
        self.return_var=StringVar()
        self.actualprice_var=StringVar()
        self.postcode_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.return_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.lateratefine_var=StringVar()
        self.finallprice_var=StringVar()

        lbltitle=Label(self.root,text="LIBRARY MANAGMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times of roman",40,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
#[lbltitle],It creates an coloum for the name library managment system and here we store all the size,style,font for the title
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=108,width=1280,height=420)
#[frame],It cretes the frame for the title given above
        #=================================DataFrameLeft================================================================  
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="black",bd=12,relief=RIDGE,font=("times of roman",14,"bold"))
        DataFrameLeft.place(x=0,y=5,width=820,height=350)
#here we are creating the label of the column of the library membership info. 
        lblmember=Label(DataFrameLeft,bg="powder blue",textvariable=self.member_var,text="Member Type:",font=("times of roman",13,"bold"),padx=2,pady=6)
#[lblmember.grid],We use grid to add the column and row in the label and here we are using both the value 0 because the default value of both is always 0 and sticky tells us the corner of that program OORR [grid] ,It is used for createing a difference between the row and column between them
        lblmember.grid(row=0,column=0,sticky=W) 
#[combobox],Here we are using combobox because we have to create a wedget of a box which will create a small wedget in which all the data's like student i'd and admin member and the leacturer i'd will show in that      
#In this we are using [state="readonly"] function which tell's us about the complete format of that column  
        comMember=ttk.Combobox(DataFrameLeft,font=("times of roman",12,"bold"),textvariable=self.member_var,width=27,state="readonly")
        comMember["value"]=("Admin Staff","Students","Lecturer")
        comMember.grid(row=0,column=1) 
#[lblPRN_NO],These are the labels of all the boxes where we will store the complete data and that will show us the complete box with the names and there boxes. and the[txtPRN_NO],Show the complete entry of the data 
        lblPRN_NO=Label(DataFrameLeft,bg="powder blue",text="PRN NO:",font=("times of roman",13,"bold"),padx=2)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
#[txtPRN_NO],It mainly creates the text box of all the boxes and they both will be showen together.
        txtPRN_NO=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.prnno_var,width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="I'D NO:",font=("times of roman",13,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstname=Label(DataFrameLeft,bg="powder blue",text="First Name:",font=("times of roman",13,"bold"),padx=2,pady=6)
        lblFirstname.grid(row=3,column=0,sticky=W)
        txtFirstname=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstname.grid(row=3,column=1)

        lblLastname=Label(DataFrameLeft,bg="powder blue",text="Last name:",font=("times of roman",13,"bold"),padx=2,pady=6)
        lblLastname.grid(row=4,column=0,sticky=W)
        txtLastname=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastname.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1:",font=("times of roman",13,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2:",font=("times of roman",13,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostcode=Label(DataFrameLeft,bg="powder blue",text="Post Code:",font=("times of roman",13,"bold"),padx=2,pady=6)
        lblPostcode.grid(row=7,column=0,sticky=W)
        txtPostcode=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostcode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile:",font=("times of roman",13,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblBookID=Label(DataFrameLeft,bg="powder blue",text="Book I'd:",font=("times of roman",13,"bold"),padx=2,pady=6)
        lblBookID.grid(row=0,column=2,sticky=W)
        txtBookID=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.bookid_var,width=29)
        txtBookID.grid(row=0,column=3)

        lblBooktitle=Label(DataFrameLeft,bg="powder blue",text="Book Title:",font=("times of roman",13,"bold"),padx=2,pady=6)
        lblBooktitle.grid(row=1,column=2,sticky=W)
        txtBooktitle=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.booktitle_var,width=29)
        txtBooktitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,bg="powder blue",text="Author:",font=("times of roman",13,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed:",font=("times of roman",13,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDueDate=Label(DataFrameLeft,bg="powder blue",text="Due Date:",font=("times of roman",13,"bold"),padx=2,pady=6)
        lblDueDate.grid(row=4,column=2,sticky=W)
        txtDueDate=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.datedue_var,width=29)
        txtDueDate.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="Days On Book:",font=("times of roman",13,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.days_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Return fine:",font=("times of roman",13,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.return_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverdate=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:",font=("times of roman",13,"bold"),padx=2,pady=6)
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        txtDateOverdate=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtDateOverdate.grid(row=7,column=3)        

        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price:",font=("times of roman",13,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("times of roman",13,"bold"),textvariable=self.actualprice_var,width=29)
        txtActualPrice.grid(row=8,column=3)

#[DataFrameLeft],It create another subframe under the (lbltitle) and we write here left because it is placed at the left side of the data and the we name it as library membership information 
        #=================================DataFrame Right===========================================================

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="black",bd=12,relief=RIDGE,font=("arial",14,"bold"))
        DataFrameRight.place(x=830,y=5,width=403,height=350)
#[self.txtBox],It is used to create a text box on the right side of the window where we will store the values
        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=18,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
#[listScrollbar=Scrollbar],This statement creates a scrollbar in the list
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
#[listbooks],This statement collectes all the names of the book which are present there and this shows us the complete data and then we create and box for the nameing[listbox=listbox],This statement shows the box for the name of all he books and the we will grid it
        listbooks=['MATLAB','Head fit book','Learn Python the hard way','Python Programming','Secrete Rahshy','Python CookBook','Into the Machine Learning','Fluent Python','My Python','Advance Python','Machine Python','Inton Python','RedChill Python','The return of hanuman','Ramayan','Mahabharat','Sunderkand','Computer Organization Architacture By Moris Manno','The 8051 Microcontrol and inbuilt system','Fundamental of computer','Fundamental of Programming Language','Information Technology','Foundation of Computer','Software Design','Computer System Architecture','Computer Network','Computer Graphics','Data Structures','Computer Organization and Architecture','Information System and Security','Core Java','DOS','Program solving and program design in C','Let us C','Internet and java Programming','C++ program design','CCNA','Expert data strucutures with C','LINUX','The theory of Computation','UNIX', 'Database system concept','Foundation of Infromational Technology','Cryptography and Network security','Visual Basic 6.0','Data mining','Opearting System','Digital Image Processing','Operating system with JAVA','OOPS with JAVA','Professional Communication','Applied Cryptography','Natural Language understanding','Ártificial Intelligence','DS with C++','Informational Security and CyberLaw','Data Structures and theory of Logics','Energy Science','Engineering Graphics','Engineering Physics','Engineering Chemistry','Engineering maths1','Engineering Maths2','Engineering Maths3','']
        
        
        def Selectbook(event=""):
            value=str(listbox.get(listbox.curselection()))
            x=value
            if(x=="MATLAB"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.return_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.788")

            elif(x=="Head fit book"):
                self.bookid_var.set("BKID54524")
                self.booktitle_var.set("Head fit book ")
                self.author_var.set("PHenerty")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.return_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.578")

            elif(x=="Learn Python the hard way"):
                self.bookid_var.set("BKID54542")
                self.booktitle_var.set("Learn Python the hard way ")
                self.author_var.set("henery")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.return_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.1788")

            elif(x=="Python Programming"):
                self.bookid_var.set("BKID54w542")
                self.booktitle_var.set("Python Programming ")
                self.author_var.set("Ben marbel")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.return_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.128")

            elif(x=="Secrete Rahshy"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("LSecrete Rahshy ")
                self.author_var.set("rohit")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.return_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.788")

            elif(x=="Python CookBook"):
                self.bookid_var.set("BKID54542")
                self.booktitle_var.set("Python CookBook ")
                self.author_var.set("cookbook")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.return_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.1788")

            elif(x=="Fluent Python"):
                self.bookid_var.set("BKID54543")
                self.booktitle_var.set("Fluent Python ")
                self.author_var.set("jorden")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.return_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.1578")

            elif(x=="My Python"):
                self.bookid_var.set("BKID54542")
                self.booktitle_var.set("My Python")
                self.author_var.set("Lem")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.return_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.588")
 
            elif(x=="Advance Python"):
                self.bookid_var.set("BKID54553")
                self.booktitle_var.set("Advance Python ")
                self.author_var.set("marry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.return_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.1238")

            elif(x=="Inton Python "):
                self.bookid_var.set("BKID542")
                self.booktitle_var.set("Inton Python ")
                self.author_var.set("NIkhil")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.return_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.1788")

            elif(x=="RedChill Python"):
                self.bookid_var.set("BKID54542")
                self.booktitle_var.set("RedChill Python")
                self.author_var.set("henry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.return_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.788")

            elif(x=="The return of hanuman"):
                self.bookid_var.set("BKID54542")
                self.booktitle_var.set("The return of hanuman ")
                self.author_var.set("devdutt")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.return_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.1598")

        listbox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=15)
        listbox.bind("<<ListboxSelect>>",Selectbook)
        listbox.grid(row=0,column=0,padx=4)
#[listScrollbar.config],This statement show us that the range of the command is already derived and here it will runn the code
        listScrollbar.config(command=listbox.yview)
#Here we are running for loop because this loop will sent all name to the selected box and here it will inserte it
        for item in listbooks:
            listbox.insert(END,item)

#[DataFrameRight],It does the save work as the above one the only difference is that it creates an subframe on the right side of the frame and name it as Book Details

        #=============================="Button's Frame"=============================================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=480,width=1280,height=60)

        ButtonAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=19,bg="blue",fg="White")
        ButtonAddData.grid(row=0,column=0)

        ButtonShowData=Button(Framebutton,text="Show Data",font=("arial",12,"bold"),width=19,bg="blue",fg="White")
        ButtonShowData.grid(row=0,column=1)

        ButtonUpdate=Button(Framebutton,text="Update",font=("arial",12,"bold"),width=19,bg="blue",fg="White")
        ButtonUpdate.grid(row=0,column=2)

        ButtonDelete=Button(Framebutton,text="Delete",font=("arial",12,"bold"),width=19,bg="blue",fg="White")
        ButtonDelete.grid(row=0,column=3)

        ButtonReset=Button(Framebutton,text="Reset",font=("arial",12,"bold"),width=19,bg="blue",fg="White")
        ButtonReset.grid(row=0,column=4)

        ButtonExit=Button(Framebutton,text="Exit",font=("arial",12,"bold"),width=19,bg="blue",fg="White")
        ButtonExit.grid(row=0,column=5)

#[Framebutton] in this we will create a small frame for the button which we will use to fill the data 
        #============================Information Frame=========================================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=530,width=1280,height=120)
#[FrameDetails] this will create a frame to store the data of the complete system
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="white")
        Table_frame.place(x=0,y=2,width=1210,height=95)
#[Table_frame] this will create a frame inside framedetails ,[ Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue") ] {Here the keyword frame is very important because it only creates the frame and all other's are the details of that}
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
#[ xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)],Here we are creating a scrollbar for that tabel from the hrizontal and vertical size of that area 
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1","address2","postid","mobile","bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=xscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
#[self.library_table=ttk.Treeview],In this we are creating a reference in the tree format with ttk library and we filled the complete data with the data's.
        self.library_table.heading("membertype",text="Member Type")
#[self.library_table.heading("membertype",text="Member Type")],Here we are making a heading file of that data and then we also set the heading name.
        self.library_table.heading("prnno",text="Reference no")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date of Borrowed")
        self.library_table.heading("datedue",text="Due Date")
        self.library_table.heading("days",text="Day's on Book")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")
#[self.library_table],Here we are presenting the complete data in the main coloum
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
#[self.library_tabel["show"="heading"]],This statement only helps us to show that data.
        self.library_table.column("membertype",width=100)
#[self.library_table.column("membertype",width=100)],Here we are only fixing the size of all the coloum
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)


    def add_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="world")
        my_cursor = conn.cursor()

        my_cursor.execute("INSERT INTO library VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                self.member_var.get(),
                self.prnno_var.get(),
                self.id_var.get(),
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.address1_var.get(),
                self.address2_var.get(),
                self.postcode_var.get(),
                self.mobile_var.get(),
                self.bookid_var.get(),
                self.booktitle_var.get(),
                self.author_var.get(),
                self.dateborrowed_var.get(),
                self.datedue_var.get(),
                self.days_var.get(),
                self.return_var.get(),
                self.dateoverdue_var.get(),
                self.finallprice_var.get()
            )
        )

        conn.commit()
        self.fetch_data() 
        conn.close()
        messagebox.showinfo("Success", "Member has been inserted successfully")

 
if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()