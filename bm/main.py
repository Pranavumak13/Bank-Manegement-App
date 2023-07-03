# imports
from tkinter import *
# creating and removing a directory (folder), fetching its contents,etc
import os
# contains support to create and modify Tkinter images
from PIL import ImageTk, Image
# import sqlite
import sqlite3


# Functions


def init_db():
    # print("hello")
    # print(os.getcwd())
    conn = sqlite3.connect('bm/bank.db')
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS customers (
    id          INTEGER PRIMARY KEY
                        UNIQUE
                        NOT NULL,
    name        TEXT    UNIQUE  NOT NULL,
    mobileNo    TEXT UNIQUE
                        NOT NULL,
    accType     TEXT    NOT NULL,
    nationality TEXT    NOT NULL,
    gender      TEXT    NOT NULL,
    balance     REAL    NOT NULL,
    password    TEXT NOT NULL
)
''')
    # Commit the changes and close the connection
    conn.commit()
    conn.close()


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
    temp_name = StringVar()
    temp_mob = IntVar()
    temp_at = StringVar()
    temp_nationality = StringVar()
    temp_gender = StringVar()
    temp_balance = IntVar()
    temp_password = StringVar()

    # Labels
    Label(register_screen, text="Please Enter the below deatils to register.",
          font=("calibri", 12), bg="#5E88FC").grid(row=0, sticky=N, pady=10)
    Label(register_screen, text="Full Name : ",
          font=("calibri", 12)).grid(row=1, sticky=W)
    Label(register_screen, text="Mobile Number : ",
          font=("calibri", 12)).grid(row=2, sticky=W)
    Label(register_screen, text="Account Type(S/C) : ",
          font=("calibri", 12)).grid(row=3, sticky=W)
    Label(register_screen, text="Nationality : ",
          font=("calibri", 12)).grid(row=4, sticky=W)
    Label(register_screen, text="Gender : ", font=(
        "calibri", 12)).grid(row=5, sticky=W)
    Label(register_screen, text="Initial Balance : ₹",
          font=("calibri", 12)).grid(row=6, sticky=W)
    Label(register_screen, text="Password : ",
          font=("calibri", 12)).grid(row=7, sticky=W)
    notif = Label(register_screen, font=("calibri", 12))
    notif.grid(row=9, sticky=N, pady=10)

    # Entries
    Entry(register_screen, textvariable=temp_name).place(x=140, y=50)
    Entry(register_screen, textvariable=temp_mob).place(x=140, y=75)
    Entry(register_screen, textvariable=temp_at).place(x=140, y=100)
    Entry(register_screen, textvariable=temp_nationality).place(x=140, y=125)
    Entry(register_screen, textvariable=temp_gender).place(x=140, y=150)
    Entry(register_screen, textvariable=temp_balance).place(x=140, y=175)
    Entry(register_screen, textvariable=temp_password,
          show="*").place(x=140, y=200)

    # Button
    Button(register_screen, text="Register", command=finish_reg,
           font=("calibri", 12)).grid(row=8, sticky=N, pady=10)


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
    # all_accounts = os.listdir()

    if name == "" or mobileNo == "" or accType == "" or nationality == "" or gender == "" or balance == "" or password == "":
        notif.config(fg="red", text="All fields are required *")
        return

    # Connect to db and create a cursor object
    conn = sqlite3.connect('bm/bank.db')
    c = conn.cursor()

    # Check if account already exists
    c.execute("SELECT * FROM customers WHERE name = ?", (name,))
    if c.fetchone() is not None:
        notif.config(fg="red", text="Account already exists")
        return

    c.execute("SELECT mobileNo FROM customers WHERE mobileNo = ?", (mobileNo,))
    if c.fetchone() is not None:
        notif.config(fg="red", text="Mobile number already exists")
        return

    # Insert the new user's data into the database
    c.execute("INSERT INTO customers (name,mobileNo,accType,nationality ,gender,balance,password) VALUES (?,?,?,?,?,?,?)",
              (name, mobileNo, accType, nationality, gender, balance, password))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    notif.config(fg="green", text="Account has been created")

    # for name_check in all_accounts:
    #     if name == name_check:
    #         notif.config(fg="red", text="Account already exists")
    #         return
    #     else:
    #         new_file = open(name, "w")
    #         new_file.write(name+"\n")
    #         new_file.write(mobileNo+"\n")
    #         new_file.write(accType+"\n")
    #         new_file.write(nationality+"\n")
    #         new_file.write(gender+"\n")
    #         new_file.write(balance+"\n")
    #         new_file.write(password)
    #         new_file.close()
    #         notif.config(fg="green", text="Account has been created.")


def deposit():
    # Variables
    global amount
    global deposit_notif
    global current_balance_label
    amount = StringVar()

    """file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[5]"""

    # Connect to db and create a cursor object
    conn = sqlite3.connect('bm/bank.db')
    c = conn.cursor()

    # Get the user's current balance from the database
    c.execute("SELECT balance FROM customers WHERE name = ?", (login_name,))
    result = c.fetchone()
    if result is not None:
        details_balance = str(result[0])

    # Close the database connection
    conn.close()

    # Deposit Screen
    deposit_scrren = Toplevel(master)
    deposit_scrren.title("Deposit")

    # Label
    Label(deposit_scrren, text="DEPOSIT", bg="#5E88FC", width="30",
          font=("calibri", 12)).grid(row=0, sticky="NESW", pady=10)
    current_balance_label = Label(
        deposit_scrren, text="Current Balance : ₹" + details_balance, font=("calibri", 12))
    current_balance_label.grid(row=1, sticky=W)
    Label(deposit_scrren, text="Amount : ₹", font=(
        "calibri", 12)).grid(row=2, sticky=W)
    deposit_notif = Label(deposit_scrren, font=("calibri", 12))
    deposit_notif.grid(row=4, sticky=N, pady=5)

    # ENtry
    Entry(deposit_scrren, textvariable=amount).place(x=80, y=75)

    # Button
    Button(deposit_scrren, text="Update", font=("calibri", 12),
           width="20", command=finish_deposit).grid(row=3, sticky=N, pady=5)


def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text="Amount is Required!", fg="red")
        return
    if float(amount.get()) <= 0:
        deposit_notif.config(text="Please Enter Positive Currency", fg="red")
        return

    """file = open(login_name, "r+")
    file_data = file.read()
    details = file_data.split("\n")
    current_balance = details[5]"""

    # Connect to db and create a cursor object
    conn = sqlite3.connect('bm/bank.db')
    c = conn.cursor()

    # Get the user's current balance from the database
    c.execute("SELECT balance FROM customers WHERE name = ?", (login_name,))
    result = c.fetchone()
    if result is not None:
        current_balance = str(result[0])

    # Update the user's balance in the database
    updated_balance = float(current_balance) + float(amount.get())
    c.execute("UPDATE customers SET balance = ? WHERE name = ?",
              (updated_balance, login_name))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    """file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()"""

    current_balance_label.config(
        text="Current Balance : ₹" + str(updated_balance), fg="green")
    deposit_notif.config(text="Balance Updated", fg='green')


def withdraw():
    # Variables
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()

    """file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[5]"""

    # Connect to db and create a cursor object
    conn = sqlite3.connect("bm/bank.db")
    c = conn.cursor()

    # Get the user's current balance from the database
    c.execute("SELECT balance FROM customers WHERE name = ?", (login_name,))
    result = c.fetchone()
    if result is not None:
        details_balance = str(result[0])

    # close the database connection
    conn.close()

    # withdraw Screen
    withdraw_scrren = Toplevel(master)
    withdraw_scrren.title("withdraw")

    # Label
    Label(withdraw_scrren, text="WITHDRAW", bg="#5E88FC", width="30",
          font=("calibri", 12)).grid(row=0, sticky="NESW", pady=10)
    current_balance_label = Label(
        withdraw_scrren, text="Current Balance : ₹" + details_balance, font=("calibri", 12))
    current_balance_label.grid(row=1, sticky=W)
    Label(withdraw_scrren, text="Amount : ₹", font=(
        "calibri", 12)).grid(row=2, sticky=W)
    withdraw_notif = Label(withdraw_scrren, font=("calibri", 12))
    withdraw_notif.grid(row=4, sticky=N, pady=5)

    # ENtry
    Entry(withdraw_scrren, textvariable=withdraw_amount).place(x=80, y=75)
    # Button
    Button(withdraw_scrren, text="Update", width="20", font=(
        "calibri", 12), command=finish_withdraw).grid(row=3, sticky=N, pady=5)


def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(text="Amount is Required!", fg="red")
        return
    if float(withdraw_amount.get()) <= 0:
        withdraw_notif.config(text="Please Enter Positive Currency", fg="red")
        return

    # file = open(login_name, "r+")
    # file_data = file.read()
    # details = file_data.split("\n")
    # current_balance = details[5]

    # Connect to db and create a cursor object
    conn = sqlite3.connect('bm/bank.db')
    c = conn.cursor()

    # Get the user's current balance from the database
    c.execute("SELECT balance FROM customers WHERE name = ?", (login_name,))
    result = c.fetchone()
    if result is not None:
        current_balance = str(result[0])

    if (float(withdraw_amount.get()) > float(current_balance)):
        withdraw_notif.config(text="Insufficient Funds!", fg="red")
        return

    # Update the user's balance in the database
    updated_balance = float(current_balance) - float(withdraw_amount.get())
    c.execute("UPDATE customers SET balance = ? WHERE name = ?",
              (updated_balance, login_name))

    # commit the changes and close the connection
    conn.commit()
    conn.close()

    # file_data = file_data.replace(current_balance, str(updated_balance))
    # file.seek(0)
    # file.truncate(0)
    # file.write(file_data)
    # file.close()

    current_balance_label.config(
        text="Current Balance : ₹" + str(updated_balance), fg="green")
    withdraw_notif.config(text="Balance Updated", fg='green')


def personal_details():
    # Variables
    """file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')"""

    # Connect to the db and create a cursor object
    conn = sqlite3.connect('bm/bank.db')
    c = conn.cursor()

    # Get the user's personal details from db
    c.execute("SELECT * FROM customers WHERE name = ?", (login_name,))
    user_details = c.fetchone()

    details_name = user_details[1]
    details_mobile = user_details[2]
    details_at = user_details[3]
    details_nationality = user_details[4]
    details_gender = user_details[5]
    details_balance = str(user_details[6])

    # close the db connection
    conn.close()

    # Personal Details Screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')

    # Labels
    Label(personal_details_screen, text="Personal Details", bg="#5E88FC",
          font=("calibri", 12), width="40").grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen, text="Name : "+details_name,
          font=("calibri", 12), width="40").grid(row=1, sticky=W)
    Label(personal_details_screen, text="Mobile Number : "+details_mobile,
          font=("calibri", 12), width="40").grid(row=2, sticky=W)
    Label(personal_details_screen, text="Account Type(S/C) : " +
          details_at, font=("calibri", 12), width="40").grid(row=3, sticky=W)
    Label(personal_details_screen, text="Nationality : "+details_nationality,
          font=("calibri", 12), width="40").grid(row=4, sticky=W)
    Label(personal_details_screen, text="Gender : "+details_gender,
          font=("calibri", 12), width="40").grid(row=5, sticky=W)
    Label(personal_details_screen, text="Balance : ₹" + details_balance,
          font=("calibri", 12), width="40").grid(row=6, sticky=W)


def login():
    # variables
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()

    # Login Screen
    login_screen = Toplevel(master)
    login_screen.title("Login")

    # Labels
    Label(login_screen, text="Login to your account", font=("calibri", 12),
          bg="#5E88FC", width=30).grid(row=0, sticky="NESW", pady=10)
    Label(login_screen, text="Username :", font=(
        "calibri", 12)).grid(row=1, sticky=W)
    Label(login_screen, text="Password :", font=(
        "calibri", 12)).grid(row=2, sticky=W)
    login_notif = Label(login_screen, font=("calibri", 12))
    login_notif.grid(row=4, sticky=N)

    # Entry
    Entry(login_screen, textvariable=temp_login_name).place(x=80, y=50)
    Entry(login_screen, textvariable=temp_login_password,
          show="*").place(x=80, y=75)
    # Button
    Button(login_screen, text="Login", font=("calibri", 12),
           command=login_session, width=15).grid(row=3, sticky=N, pady=5, padx=5)


def login_session():
    global login_name
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    # all_accounts = os.listdir()
    """ for name in all_accounts:
        if name == login_name:
            file = open(name, "r")
            file_data = file.read()
            file_data = file_data.split("\n")
            password = file_data[6]

            # Account Dashboard
            if login_password == password:"""

    # Connect to the db and create a cursor object
    conn = sqlite3.connect('bm/bank.db')
    c = conn.cursor()

    # Check if a user with the entered username and password exists in the database
    c.execute("SELECT * FROM customers WHERE name = ? AND password = ?",
              (login_name, login_password))

    if c.fetchone() is not None:
        # Account Dashboard
        login_screen.destroy()
        account_dashboard = Toplevel(master)
        account_dashboard.title('Dashboard')

        # Labels
        Label(account_dashboard, text="Account Dashboard", bg="#5E88FC",
              font=("calibri", 12), width="40").grid(row=0, sticky=N, pady=10)
        Label(account_dashboard, text="Welcome " + login_name + " :)",
              font=("calibri", 12)).grid(row=1, sticky=N, pady=5)

        # Buttons
        Button(account_dashboard, text="Personal Details", font=("calibri", 12),
               width="30", command=personal_details).grid(row=2, sticky=N, padx=10)
        Button(account_dashboard, text="Deposit", font=("calibri", 12),
               width="30", command=deposit).grid(row=3, sticky=N, padx=10)
        Button(account_dashboard, text="Withdraw", font=("calibri", 12),
               width="30", command=withdraw).grid(row=4, sticky=N, padx=10)
        Label(account_dashboard).grid(row=5, sticky=N, pady=10)
        return

    # Close the database connection
    conn.close()

    login_notif.config(fg="red", text="Invalid username or password")


# Initialize the database
init_db()

# Main Screen
master = Tk()
master.title("Banking App")
master.geometry("325x400")

# Image Imports

img = Image.open('Images/Bank.jpg')
img = img.resize((300, 187))
img = ImageTk.PhotoImage(img)

# Labels
Label(master, text="VOICE BANK", bg="#5E88FC", font=(
    "Segoe UI", 14)).grid(row=0, sticky="NESW", pady=10)
Label(master, text="The Most Secure Bank you have Ever Seen",
      font=("calibri", 12)).grid(row=1, sticky="NESW")
Label(master, image=img).grid(row=2, sticky="NESW", pady=15, padx=10)

# Button
Button(master, text="Register", font=("calibri", 12),
       width=20, command=Register).grid(row=3, sticky=N)
Button(master, text="Login", font=("calibri", 12), width=20,
       command=login).grid(row=4, sticky=N, pady=10)

master.mainloop()
