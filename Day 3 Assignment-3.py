#importing library
from tkinter import *
from tkinter import ttk

window = Tk()
#Declaring Window Title
window.title("Registration Form")
#Declaring Window size
window.geometry('800x800')
#Declaring Window Color
window.configure(background = "lightGrey");
#below four fields are declared
label_1 = Label(window, text="EMPLOYEE REGISTER FORM",width=30,font=("bold", 10)).grid(row=0, column=4)
FirstName = Label(window, text="First Name :",width=20,font=("bold", 10)).grid(row=1, column=1)
LastName = Label(window, text="Last Name :",width=20,font=("bold", 10)).grid(row=2, column=1)
RegisterId= Label(window, text="Reg.Id :",width=20,font=("bold", 10)).grid(row=3, column=1)
EmailId=Label(window, text="E-mail Id :",width=20,font=("bold", 10)).grid(row=4 , column=1)
MobileNo=Label(window, text="Mobile No. :",width=20,font=("bold", 10)).grid(row=5, column=1)
DOB=Label(window, text="Date of Birth",width=20,font=("bold", 10)).grid(row=6, column=1)
Gender=Label(window, text="Gender :",width=20,font=("bold", 10)).grid(row=7, column=1)
var = IntVar()
Radiobutton(window, text="Male",padx = 30, variable=var, value=1).grid(row=7,column=2)
Radiobutton(window, text="Female",padx = 30, variable=var, value=2).grid(row=7,column=3)
Address=Label(window, text="Address :",width=20,font=("bold",10)).grid(row=8,column=1)
City=Label(window, text="City :",width=20,font=("bold", 10)).grid(row=9,column=1)
Country=Label(window, text="Country :",width=20,font=("bold",10)).grid(row=10,column=1)
list=["INDIA","GERMANY","USA","UK","AUSTRALIA","CANADA","OTHER"]
c=StringVar()
droplist=OptionMenu(window,c,*list)
droplist.config(width=20)
c.set("Select Your Country")
droplist.grid(row=10,column=2)
Postalcode=Label(window, text="Postal Code :",width=20,font=("bold",10)).grid(row=11,column=1)
Programming=Label(window, text="Select the Known Programming :",font=("bold",10)).grid(row=12,column=1)
Checkbutton1 = IntVar()
Checkbutton(window, text="Python",variable= Checkbutton1,onvalue=1,offvalue=0,height=2,width=10).grid(row=12,column=2)
Checkbutton2 = IntVar()
Checkbutton(window, text="HTML",variable= Checkbutton2,onvalue=1,offvalue=0,height=2,width=10).grid(row=12,column=3)
Checkbutton3 = IntVar()
Checkbutton(window, text="JS",variable= Checkbutton,onvalue=1,offvalue=0,height=2,width=10).grid(row=12,column=4)
Checkbutton4= IntVar()
Checkbutton(window, text="PHP",variable= Checkbutton,onvalue=1,offvalue=0,height=2,width=10).grid(row=12,column=5)

FirstName=Entry(window).grid(row=1,column=2)
LastName=Entry(window).grid(row=2,column=2)
RegisterId=Entry(window).grid(row=3,column=2)
EmailId=Entry(window).grid(row=4,column=2)
MobileNo=Entry(window).grid(row=5,column=2)
DOB=Entry(window).grid(row=6,column=2)
Address=Entry(window).grid(row=8,column=2)
City=Entry(window).grid(row=9,column=2)
Postalcode=Entry(window).grid(row=11,column=2)

def onClick():
    print("Your Details has been Successfully saved")


# Create a Button
Button(window, text="Submit", command=onClick,width=20,bg='Grey',fg='Skyblue').grid(row = 13,column = 3)
window.mainloop()






