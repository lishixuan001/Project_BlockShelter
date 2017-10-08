import tkinter as tk
from tkinter import messagebox
import pickle

class LoginSignup(Object):

    """
    Define the class name and class attribute
    """
    def __init__(name='LoginSignup', attr='CommandClass'):
        self.name = name
        self.attr = attr

    """
    Command Function for Login button
    """
    def user_login(self, var_user_name, var_user_password):
        # Get the user input information
        user_name = var_user_name.get()
        user_password = var_user_password.get()

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
