#!/usr/bin/env python

""" Search destination page """

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
imgPath = 'fun.gif'
image_file = tk.PhotoImage(file=imgPath)
label = tk.Label(window, image = image_file).place(x=225, y=150, anchor='center')

"""
User Input (Part I) --Lable
"""
# Define text --"What's your destination?"
tk.Label(window, text='Please enter your destination', font=14, fg='red').place(x=225, y=80, anchor='center')


"""
User Input (Part II) --Entry
"""
# Define input variable --var_my_destination
var_my_destination = tk.StringVar()
# Set example input variable
var_my_destination.set('(ex: Haas Business School)')
# Define entry --entry_my_destination
entry_my_destination = tk.Entry(window, textvariable=var_my_destination)
# Place entry --entry_my_destination
entry_my_destination.place(x=225, y=120, anchor='center')


"""
Command Function for button_destination_confirm
"""
def check_valid_and_continue():
    # Get user's input
    my_destination = var_my_destination.get()
    # Try open the destination info document

    try:
        # If it exist, then load its information
        with open('destinations_info.pickle', 'rb') as destination_file:
            destinations_info = pickle.load(destination_file)
    except FileNotFoundError:
        # If it doesn't exist, create one
        with open('destinations_info.pickle', 'wb') as destination_file:
            # Write in default user 'admin'
            destinations_info = {'sample': {'public': {'location_public': ['info']},
                                            'shared': {'location_shared': ['info']}}}
            pickle.dump(destinations_info, destination_file)

    # Check if user input is in our date base
    if my_destination not in destinations_info:
        # If it doesn't, then report sorry (error)
        tk.messagebox.showerror(message='Sorry. The destination is not yet included in our service.')

        '''
        Add-on: Keep track of users' needs in destination which we don't support
        '''
        # Write the destination into the record database
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
        # Add the undocumented destination to request list database
        length_of_destinations_requests_info = len(destinations_requests_info)
        index = length_of_destinations_requests_info
        # Do the plug in
        destinations_requests_info[string(index)] = my_destination

    # If it does, then goto next window that show the search results
    else:
        # Make a place to save the choice
        try:
            # If it exist, then load its information
            # and change the 'choice'
            with open('my_choice_info.pickle', 'rb') as my_choice_file:
                my_choice_info = pickle.load(my_choice_file)
                my_choice_info['choice'] = my_destination
        except FileNotFoundError:
            # If it doesn't exist, create one
            with open('my_choice_info.pickle', 'wb') as my_choice_file:
                # Write in current 'choice'
                my_choice_info = {'choice': my_destination}
                pickle.dump(my_choice_info, my_choice_file)

        # Close current and open the later window
        window.destroy()
        os.system('python gui_search_result.py')



"""
Button --button_destination_confirm
"""
# Define Button
button_destination_confirm = tk.Button(window, text='Confirm', bg='yellow',
                                       command=check_valid_and_continue)

# Place button
button_destination_confirm.place(x=225, y=180, anchor='center')




window.mainloop()




### keep track of user behavior
# which destination is searched the most?
# change => as the example
