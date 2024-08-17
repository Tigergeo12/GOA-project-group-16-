import random
import tkinter as tk
from tkinter import messagebox

length = 12 # password length

def generate_password():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()" # usable chars for pass
    
    Password = []
    for i in range(length):  
        Password.append(random.choice(chars)) #generating the random password

    password_entry.delete(0, tk.END)  # Clearring the textbox in the tk
    password_entry.insert(tk.END, ''.join(Password))  # Inserting the generates password into the tk window

root = tk.Tk() # making the window
root.title("Password Generator")

password_label = tk.Label(root, text="Password:")
password_label.pack() #design

password_entry = tk.Entry(root, width=50)
password_entry.pack() #design / size of window

generate_button = tk.Button(root, text="Generate Password", command=generate_password) #importing the def function into the actual window
generate_button.pack() # the button to adtually make it work

root.mainloop() # runnning the window