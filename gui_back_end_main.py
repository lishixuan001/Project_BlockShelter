#!/usr/bin/env python

"""
Choose from three main accesses for Admin
"""

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
import webbrowser

"""
Start defining new window
Let user input the destination
"""
window = tk.Tk()
window.title('Main Page BlockShelter')
window.geometry('450x300')


"""
The background image
"""
imgPath = 'choose.gif'
image_file = tk.PhotoImage(file=imgPath)
label = tk.Label(window, image = image_file).place(x=225, y=200, anchor='center')


"""
Command Function: check_requests
Command Function: check_current
"""
def check_requests():
    window.destroy()
    os.system('python gui_back_end_requests.py')

def check_current():
    window.destroy()
    os.system('python gui_back_end_database.py')

def check_detect():
    window.destroy()
    os.system('python gui_back_end_detection.py')


"""
Button --button_requests
Button --button_current
Button --button_detect
"""
# Define Button
button_requests = tk.Button(window, text='Check Requests', bg='blue',
                                  font=16, fg='yellow', command=check_requests)

button_current = tk.Button(window, text='Check Database', bg='blue',
                                  font=16, fg='yellow', command=check_current)

button_detect = tk.Button(window, text='Check Detection', bg='blue',
                                  font=16, fg='yellow', command=check_detect)

# Place button
button_requests.place(x=110, y=130, anchor='center')
button_current.place(x=340, y=130, anchor='center')
button_detect.place(x=225, y=170, anchor='center')




window.mainloop()
