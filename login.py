import hashlib
from tkinter import *
from tkinter import messagebox
from firebase import firebase

registration_window = Tk()
registration_window.geometry("400x400")
registration_window.title("Sign Up")
registration_window.configure(background = "orange")

firebase = firebase.FirebaseApplication("https://project---188-default-rtdb.fi...", None)

login_username_entry = ""
login_password_entry = ""

def login(): 
    print("Login Function")
    
    global login_password_entry
    global login_username_entry
    
    username = login_username_entry.get()
    password = login_password_entry.get()
    
    encrypted_password = hashlib.md5(password.encode())
    hexadecimal_password = encrypted_password.hexdigest()
    get_password = firebase.get("/", username)
    print(hexadecimal_password)
    
    if(get_password != None):
        if(get_password == hexadecimal_password):
            messagebox.showinfo("Information", "Successfully Logged In")
        else:
            messagebox.showinfo("Information", "Please Check Your Password")
    else:
        messagebox.showinfo("Information", "User Not Registered! \n Get Yourself Registered 1st To Login")
    
def register(): 
    print("Register Function")
    
    username = username_entry.get()
    password = password_entry.get()
    
    encrypted_password = hashlib.md5(password.encode())
    hexadecimal = encrypted_password.hexdigest()
    print(hexadecimal)
    firebase.put("/", username, hexadecimal)
    
    messagebox.showinfo("Information", "Successfully Registered")
    
def login_window():
    global login_username_entry
    global login_password_entry
    
    registration_window.destroy()
    
    login_window = Tk()
    login_window.geometry("400x400")
    login_window.title("Log In")
    login_window.configure(background = "yellow")
    
    login_heading_lbl = Label(login_window, text = "Log In", font = 'arial 18 bold', fg = "black", bg = "yellow")
    login_heading_lbl.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    
    login_username_lbl = Label(login_window, text = "Username :", font = 'arial 13', bg = "yellow", fg = "black")
    login_username_lbl.place(relx = 0.3, rely = 0.5, anchor = CENTER)
    
    login_username_entry = Entry(login_window)
    login_username_entry.place(relx = 0.7, rely = 0.5, anchor = CENTER)
    
    login_password_lbl = Label(login_window, text = "Password :", font = 'arial 13', bg = "yellow", fg = "black")
    login_password_lbl.place(relx = 0.3, rely = 0.6, anchor = CENTER)
    
    login_password_entry = Entry(login_window)
    login_password_entry.place(relx = 0.7, rely = 0.6, anchor = CENTER)
    
    btn_login = Button(login_window, text = "Log In", font = 'arial 13 bold', command = login, relief = FLAT, fg = "white", bg = "black")
    btn_login.place(relx = 0.5, rely = 0.8, anchor = CENTER)
    
    login_window.mainloop()
    
heading_lbl = Label(registration_window, text = "Register", font = 'arial 18 bold', fg = "black", bg = "orange")
heading_lbl.place(relx = 0.5, rely = 0.3, anchor = CENTER)

username_lbl = Label(registration_window, text = "Username :", font = 'arial 13', bg = "orange", fg = "black")
username_lbl.place(relx = 0.3, rely = 0.5, anchor = CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx = 0.7, rely = 0.5, anchor = CENTER)

password_lbl = Label(registration_window, text = "Password :", font = 'arial 13', bg = "orange", fg = "black")
password_lbl.place(relx = 0.3, rely = 0.6, anchor = CENTER)

password_entry = Entry(registration_window)
password_entry.place(relx = 0.7, rely = 0.6, anchor = CENTER)

btn_register = Button(registration_window, text = "Sign Up", font = 'arial 13 bold', command = register, relief = FLAT, padx = 10, fg = "white", bg = "black")
btn_register.place(relx = 0.5, rely = 0.8, anchor = CENTER)

btn_login_window = Button(registration_window, text = "Log In", font = 'arial 10 bold', command = login_window, relief = FLAT, fg = "white", bg = "black")
btn_login_window.place(relx = 0.9, rely = 0.1, anchor = CENTER)

registration_window.mainloop()
