#!/usr/bin/env python

""" Main page: Choose what you want to do """

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
Command Function: do_detect
Command Function: do_search
"""
def do_detect():
    '''Get signal for parking database network nearby'''
    pass

def do_search():
    window.destroy()
    os.system('python gui_search_destination.py')


"""
Button --button_detect (Detect Parking)
Button --button_search (Search Parking)
"""
# Define Button
button_detect = tk.Button(window, text='Detect Parking', bg='blue',
                                  font=16, fg='yellow', command=do_detect)

button_search = tk.Button(window, text='Search Parking', bg='blue',
                                  font=16, fg='yellow', command=do_search)

# Place button
button_detect.place(x=110, y=135, anchor='center')
button_search.place(x=340, y=135, anchor='center')







window.mainloop()
