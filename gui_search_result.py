#!/usr/bin/env python

""" Search result page """

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
Background image
"""
imgPath = 'car.gif'
image_file = tk.PhotoImage(file=imgPath)
label = tk.Label(window, image = image_file).place(x=225, y=150, anchor='center')


"""
User Input (Part I) --Lable
"""
# Define text --"Here's what we got for you"
tk.Label(window, text='Here\'s what we got for you', font=16, fg='red').place(x=225, y=50, anchor='center')
# Define text --"Public Parking"
tk.Label(window, text='Public Parking', font=14, fg='orange').place(x=110, y=80, anchor='center')
# Define text --"Community Shared"
tk.Label(window, text='Community Shared', font=14, fg='orange').place(x=340, y=80, anchor='center')


"""
Canvas: draw line in middle
"""
# # Define a cnavas, put it in middle
# canvas = tk.Canvas(window,height=120, width=10)
# # Define the position of the line
# x0, y0, x1, y1 = 5, 0, 5, 120
# line = canvas.create_line(x0, y0, x1, y1)
# # Place the canvas
# canvas.place(x=225, y=150, anchor='center')


"""
Display the Recommands
"""
# Display choices for the public parkings
# Get the choice
with open('my_choice_info.pickle', 'rb') as my_choice_file:
    my_choice = pickle.load(my_choice_file)
    chosen_destination = my_choice['choice']

# Get the database
with open('destinations_info.pickle', 'rb') as destination_file:
    destinations_info = pickle.load(destination_file)

# Get the data from destinations_info
data_for_the_destination = destinations_info[chosen_destination]
# Get the public and the shared data seperately
public_availables = data_for_the_destination['public']
shared_availables = data_for_the_destination['shared']
# Get the names for available parking lots
public_parking_lots = []
shared_parking_lots = []
for key in public_availables:
    public_parking_lots.append(key)
for key in shared_availables:
    shared_parking_lots.append(key)

# Define Texts --public --shared
text_public = tk.Text(window, height=10, width=16)
text_shared = tk.Text(window, height=10, width=16)

# Insert values
for spot_name in public_parking_lots:
    text_public.insert('end', "\n{0}".format(spot_name))
for spot_name in shared_parking_lots:
    text_shared.insert('end', "\n{0}".format(spot_name))

# Disable users' changes
text_public.config(state='disabled')
text_shared.config(state='disabled')

# Place the texts
text_public.place(x=110, y=85, anchor='n')
text_shared.place(x=340, y=85, anchor='n')


"""
Command Function: view_the_public_map
Command Function: view_the_shared_map
"""
def view_the_public_map():
    # # Note: [python3 -m http.server] ==> command that create localhost 8080
    ''' Uncomment this when mark_map.html is available'''
    # webbrowser.open("mark_map.html")
    pass

def view_the_shared_map():
    ''' This is the method that shows information of the shared spots'''
    pass


"""
Button: button_view_public_map  --"View in map"
Button: button_view_shared_map  --"View in map"
"""
# Define Buttons
button_view_public_map = tk.Button(window, text='View in map', bg='yellow',
                                   fg='green', command=view_the_public_map)

button_view_shared_map = tk.Button(window, text='View in map', bg='yellow',
                                   fg='green', command=view_the_shared_map)

# Place the Buttons
button_view_public_map.place(x=110, y=230, anchor='center')
button_view_shared_map.place(x=340, y=230, anchor='center')





window.mainloop()
