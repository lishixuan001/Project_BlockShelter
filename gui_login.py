#!/usr/bin/env python

""" Login & Signup windows """
""" Hiden: Jump to Admin login page by entering secret_code """

__author__ = "Shixuan Li"
__credits__ = "Shixuan Li"
__version__ = "1.0.1"
__maintainer__ = "Shixuan Li"
__email__ = "lishixuan001@berkeley.edu"
__status__ = "Test"

import tkinter as tk
from tkinter import messagebox
import pickle
import os

"""
Start defining new window
"""
window = tk.Tk()
window.title('Welcome to BlockShelter')
window.geometry('450x300')


"""
Start setting the image 'Welcome'
"""
# Define Canvas --Image 'welcome.gif'
canvas = tk.Canvas(window, height=200, width=500)
# Set image path
imgPath = 'welcome.gif'
# Define the image file
image_file = tk.PhotoImage(file=imgPath)
# Create the image for canvas
image = canvas.create_image(10,0, anchor='nw', image=image_file)
# Pack the canvas
canvas.pack(side='top')


"""
User Input (Part I) --Lable
"""
tk.Label(window, text='Username: ').place(x=50, y= 150)
tk.Label(window, text='Password: ').place(x=50, y= 190)


"""
User Input (Part II) --Entry
"""
# Define input variable --Username
var_user_name = tk.StringVar()
# Define input variable --Password
var_user_password = tk.StringVar()

# Set example input variable
var_user_name.set('gobears@calhack.com')

# Define entry --Username
entry_user_name = tk.Entry(window, textvariable=var_user_name)
# Define entry --Password
entry_user_password = tk.Entry(window, textvariable=var_user_password, show='*')

# Place the entry --Username
entry_user_name.place(x=160, y=150)
# Place the entry --Password
entry_user_password.place(x=160, y=190)



"""
Command Function for Login button
"""
def user_login():
    # Get the user input information
    user_name = var_user_name.get()
    user_password = var_user_password.get()

    '''
    Admin Login Secret_Code: admin_login
    '''
    secret_code = 'admin_login'
    code = user_name
    if code == secret_code:
        window.destroy()
        os.system('python gui_back_end_login.py')

    # Try open the user info document
    try:
        # If it exist, then load its information
        with open('users_info.pickle', 'rb') as user_file:
            users_info = pickle.load(user_file)
    except FileNotFoundError:
        # If it doesn't exist, create one
        with open('users_info.pickle', 'wb') as user_file:
            # Write in default user 'admin'
            users_info = {'admin': 'admin'}
            pickle.dump(users_info, user_file)

    # See if the user input is registered in the system
    if user_name in users_info:
        # Check user's password
        if user_password == users_info[user_name]:
            # If correct, send congrads and say hi (use showinfo)
            congrads_words = 'Welcome to BlockShelter! ' + user_name + '\nHow are you~'
            tk.messagebox.showinfo(title='Welcome to BlockShelter', message=congrads_words)
            window.destroy()
            os.system('python gui_main.py')
        else:
            # If incorrect, pop window (use error)
            tk.messagebox.showerror(message='Oops, your password is wrong, try again.')
    else:
        # If the user is not registered, then pop up a window asking if he/she wants to
        # sign up an account or not (use yes/no)
        is_sign_up = tk.messagebox.askyesno(title='Notice from BlockShelter',
                               message='You have not signed up yet. Sign up today?')
        # If the user wants to sign up, lead him/her to sign-up page
        if is_sign_up:
            user_sign_up()
            is_sign_up.destroy()


"""
Command Function for Signup button
"""
def user_sign_up():
    '''
    Command Function for First-time Signin after Sign-up
    '''
    def check_the_sign_up():
        '''
        Firstly, check if the sign-up is valid
        '''
        # Get new sign-uped user information
        new_user_name = var_new_user_name.get()
        new_password = var_new_password.get()
        new_password_confirm = var_new_password_confirm.get()

        # Try open the user info document
        try:
            # If it exist, then load its information
            with open('users_info.pickle', 'rb') as user_file:
                users_info = pickle.load(user_file)
        except FileNotFoundError:
            # If it doesn't exist, create one
            with open('users_info.pickle', 'wb') as user_file:
                # Write in default user 'admin'
                users_info = {'admin': 'admin'}
                pickle.dump(users_info, user_file)

        # Check if the two passwords inputed are the same
        if new_password != new_password_confirm:
            tk.messagebox.showerror(title='Notice from BlockShelter',
                                    message='Password and confirm password must be the same!')
        # Check if new name in user info document
        elif new_user_name in users_info:
            tk.messagebox.showerror(title='Notice from BlockShelter',
                                    message='The user has already signed up!')
        else:
            # If valid, write new user's info in database
            users_info[new_user_name] = new_password
            with open('users_info.pickle', 'wb') as user_file:
                pickle.dump(users_info, user_file)
            # Pop up new window for congrads
            tk.messagebox.showinfo(title='Welcome to BlockShelter',
                                   message='You have successfully signed up!')
            sign_up_window.destroy()

    # Pop up new window for new account registration
    # Define the window (Toplevel=window)
    sign_up_window = tk.Toplevel(window)
    sign_up_window.title('Sign up window')
    sign_up_window.geometry('350x200')

    '''Set the text for user inputs'''
    ##[1] Username
    # Define new variable --username
    var_new_user_name = tk.StringVar()
    # Give example --username
    var_new_user_name.set('example@python.com')
    # Text for input box --username
    tk.Label(sign_up_window, text='User name: ').place(x=10, y= 10)
    # User entry --username
    entry_var_new_user_name = tk.Entry(sign_up_window, textvariable=var_new_user_name)
    # Place the entry
    entry_var_new_user_name.place(x=150, y=10)

    ## [2] Password
    # Define new variable --password
    var_new_password = tk.StringVar()
    # Text for input --password
    tk.Label(sign_up_window, text='Password: ').place(x=10, y=50)
    # User entry --password
    entry_user_password = tk.Entry(sign_up_window, textvariable=var_new_password, show='*')
    # Place the entry
    entry_user_password.place(x=150, y=50)

    ## [3] Confirm Password
    # Define new variable --confirm password
    var_new_password_confirm = tk.StringVar()
    # Text for input --confirm password
    tk.Label(sign_up_window, text='Confirm password: ').place(x=10, y= 90)
    # User entry --confirm password
    entry_user_password_confirm = tk.Entry(sign_up_window, textvariable=var_new_password_confirm, show='*')
    # Place the entry
    entry_user_password_confirm.place(x=150, y=90)

    # Define a button called 'Sign up'
    button_sign_up_window_sign_up = tk.Button(sign_up_window, text='Sign up', command=check_the_sign_up)
    button_sign_up_window_sign_up.place(x=150, y=130)

"""
Buttons --Login --Signup
"""
# Define button --Login
button_login = tk.Button(window, text='Login', command=user_login)
# Define button --Signup
button_sign_up = tk.Button(window, text='Sign up', command=user_sign_up)
# Place button --Login
button_login.place(x=170, y=230)
# Place button --Signup
button_sign_up.place(x=270, y=230)


window.mainloop()


### Login Function
# if the pickle file doesn't exsit, now it write in 'admin'
# change => set default 'admin' in the first place to avoid accident hack-in

### Signup/Login Function
# the username is atually email
# change => send email verification (later versions)

### Lock the login after 3 tries
# change => as stated
