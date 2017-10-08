#!/usr/bin/env python

""" Back end check requests """

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
Define Lable
"""
# Define text --"Here's what we got for you"
tk.Label(window, text='Here\'s most recent requests', font=18, fg='red').place(x=225, y=50, anchor='center')


"""
Access the data in requests
"""
try:
    # If it exist, then load its information
    with open('destinations_requests_info.pickle', 'rb') as destination_requests_file:
        destinations_requests_info = pickle.load(destination_requests_file)
except FileNotFoundError:
    # If it doesn't exist, create one
    with open('destinations_requests_info.pickle', 'wb') as destination_requests_file:
        # Write in default user 'admin'
        destinations_requests_info = {'0': 'admin'}
        pickle.dump(destinations_requests_info, destination_requests_file)

# Get the data from destinations_requests_info
index_for_requests = []
for key in destinations_requests_info:
    index_for_requests.append(key)

# Define Texts --public --shared
text_requests_display = tk.Text(window, height=15, width=25)

# Insert values
for key in index_for_requests:
    requested_location = destinations_requests_info[key]
    text_requests_display.insert('end', "\n{0}".format(requested_location))

# Disable users' changes
text_requests_display.config(state='disabled')

# Place the texts
text_requests_display.place(x=225, y=80, anchor='n')




window.mainloop()
