# Bank-Manegement-App
Banking Management System
Project in python with use of Tkinter GUI toolkit

Packages required
Tkinter - Tkinter is the standard GUI library for Python.
OS - The OS module in Python provides functions for interacting with the operating system.
Pillow - The pillow module required for fetching the images.


Installation
Tkinter
 We just need to install Python from www.python.org, and it comes along with Python.
We do not need to install it separately.

OS
 We just need to install Python from www.python.org, and it comes along with Python.
We do not need to install it separately.

Usage
import os
from datetime import date
import tkinter as tk 
from tkinter import *
Execution flow (How to run the program?)
Option 1
1. First extract the zip file.
2. Navigate to the file mainProject.py
3. Launch the code in any of the supporting IDE/code editors. (You must have python pre-installed in your system)
4. Run the code.
5. Now you are ready to interact with our python-based GUI program.
Option 2
1. First extract the zip file.
2. Navigate to the path containing extracted folder.
3. Here you can see one file named as mainProject.py
4. Now click on the location bar of Windows Explorer.
5. Then type cmd and press Enter key.
6. The command prompt will be opened in the folder.
7. Type "python mainProject.py" on command line (You must have python pre- installed in your system).
8. Now you are ready to interact with our python-based GUI program.

Features of program
This is a GUI-based program. Once started running, it will prompt users to ask whose role they want to play. According to the selection, the program will ask for credentials. Once the credentials are matched, the program will unlock the respective functions

1) Register
>> Can create a new account
> Functionalities:
                 1. Create bank account
                    - Account type
                    - Name
                    - Gender
                    - Nationality
                    - PIN
                    - DOB
                    - Mobile number
                    - Initial account balance
                    Above mentioned details are typed into the form.
                 
                 
2) Login            
>> Customer account name and PIN should be entered
> If account name and PIN matches then customer will unlock his/her
functionalities. If they don’t match or entered account number doesn't exist then appropriate error prompts are displayed.
> Functionalities:
                 1. Deposit
                    balance is updated with the new amount.
                    - Valid amount i.e., amount cannot be negative and zero
                    If above criteria are satisfied then amount is deposited
                 2. Withdraw
                    - Valid amount i.e., amount cannot be greater than total balance, negative or zero is not allowed
                    - If above criteria are satisfied then amount is withdrawn
                 3. Check your balance
                    - On pressing this button, the total balance of customer
                 
