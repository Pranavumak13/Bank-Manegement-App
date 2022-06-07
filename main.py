# imports
from tkinter import *
import os
from turtle import st
from PIL import ImageTk, Image

# Main Screen
master = Tk()
master.title("Banking App")
master.geometry("325x400")

# Functions
def finish_reg():
    name = temp_name.get()
    mobileNo = temp_mob.get()
    mobileNo = str(mobileNo)
    accType = temp_at.get()
    nationality = temp_nationality.get()
    gender = temp_gender.get()
    balance = temp_balance.get()
    balance = str(balance)
    password = temp_password.get()
    all_accounts = os.listdir()
    
    if name == "" or mobileNo == "" or accType == "" or nationality == "" or gender == "" or balance == "" or password== "":
        notif.config(fg="red", text="All fields are required *")
        return
    
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red", text="Account already exists")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+"\n")
            new_file.write(mobileNo+"\n")
            new_file.write(accType+"\n")
            new_file.write(nationality+"\n")
            new_file.write(gender+"\n")
            new_file.write(balance+"\n")
            new_file.write(password+"\n")
            new_file.close()
            notif.config(fg="green", text="Account has been created.")

def Register():
    # Register Screen
    register_screen = Toplevel(master)
    register_screen.title("Register")
    
    # Variables
    global temp_name
    global temp_mob
    global temp_at
    global temp_nationality
    global temp_gender
    global temp_balance
    global temp_password
    global notif
    temp_name=StringVar()
    temp_mob=IntVar()
    temp_at=StringVar()
    temp_nationality=StringVar()
    temp_gender=StringVar()
    temp_balance=IntVar()
    temp_password=StringVar()
    
    
    # Labels
    Label(register_screen, text="Please Enter the below deatils to register.", font=("calibri", 12)).grid(row=0, sticky=N, pady=10)
    Label(register_screen, text="Full Name : ", font=("calibri", 12)).grid(row=1, sticky=W)
    Label(register_screen, text="Mobile Number : ", font=("calibri", 12)).grid(row=2, sticky=W)
    Label(register_screen, text="Account Type(S/C) : ", font=("calibri", 12)).grid(row=3, sticky=W)
    Label(register_screen, text="Nationality : ", font=("calibri", 12)).grid(row=4, sticky=W)
    Label(register_screen, text="Gender : ", font=("calibri", 12)).grid(row=5, sticky=W)
    Label(register_screen, text="Initial Balance : ", font=("calibri", 12)).grid(row=6, sticky=W)
    Label(register_screen, text="Password : ", font=("calibri", 12)).grid(row=7, sticky=W)
    notif = Label(register_screen, font=("calibri", 12))
    notif.grid(row=9, sticky=N, pady=10)
    
    # Entries
    Entry(register_screen, textvariable=temp_name).place(x=140, y=50)
    Entry(register_screen, textvariable=temp_mob).place(x=140, y=75)
    Entry(register_screen, textvariable=temp_at).place(x=140, y=100)
    Entry(register_screen, textvariable=temp_nationality).place(x=140, y=125)
    Entry(register_screen, textvariable=temp_gender).place(x=140, y=150)
    Entry(register_screen, textvariable=temp_balance).place(x=140, y=175)
    Entry(register_screen, textvariable=temp_password, show="*").place(x=140, y=200)
    
    # Button 
    Button(register_screen, text="Register", command = finish_reg, font =("calibri", 12)).grid(row=8, sticky=N, pady=10)

# Image Imports
img = Image.open('bm/Bank.jpg')
img = img.resize((300,187))
img = ImageTk.PhotoImage(img)

# Labels
Label(master, text="VOICE BANK",bg="#5E88FC", font=("Segoe UI", 14)).grid(row=0, sticky="NESW", pady=10)
Label(master, text="The Most Secure Bank you have Ever Seen", font=("calibri", 12)).grid(row=1,sticky="NESW" )
Label(master, image=img).grid(row=2, sticky="NESW", pady=15, padx=10)

# Button
Button(master, text="Register", font=("calibri", 12), width=20, command=Register).grid(row=3,sticky=N )
Button(master, text="Login", font=("calibri", 12), width=20).grid(row=4,sticky=N, pady=10 )
master.mainloop()

