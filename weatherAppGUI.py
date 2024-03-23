from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder 
from datetime import *
import pytz
from PIL import Image, ImageTk

from getINFO import getWeather

# Create a window
root = Tk()
root.title("Look, the Weather!")
root.geometry("890x470+300+300")  # The format is width x height + x_offset + y_offset
root.configure(bg="#747474")
root.resizable(False, False)  # Window not resizable

# Round_box = PhotoImage(file="")

Label(root, bg="#707070").place(x=30, y=110)

# Labels for weather information
labels_text = ["Temperature", "Humidity", "Pressure", "Wind Speed", "Description"]
for idx, text in enumerate(labels_text):
    Label(root, text=text, font=("Arial", 11), bg="#747474").place(x=50, y=120 + (idx * 20))

# Search box
textfield = Entry(root, justify='center', width=15, font=("poppins", 25, 'bold'), bg="#444444", border=0)
textfield.place(x=370, y=130)
textfield.focus()  # Focus by default
# Bind the Enter key to call the function
textfield.bind("<Return>", lambda event: getWeather(textfield.get(), clock, timezone))

# Button boxes
frame = Frame(root, width=900, height=180, bg="#747474", border=0)
frame.pack(side=BOTTOM)

# Create a Canvas widget inside the frame
canvas = tk.Canvas(frame, width=900, height=180, bg="#747474", border=0)
canvas.pack()

# Define the number of rectangles and spacing
num_rectangles = 7
spacing = 10

# Calculate the width of each rectangle, including spacing
rect_width = (880 - (num_rectangles + 1) * spacing) / num_rectangles

# Position of the rectangles vertically
y1 = 30
y2 = 180 - 30  # Height of the frame minus spacing from top and bottom

# Define initial x-coordinate
x1 = spacing

# Draw seven rectangles
for _ in range(num_rectangles):
    # Calculate x2 based on x1 and rect_width
    x2 = x1 + rect_width
    # Create the rectangle on the canvas
    canvas.create_rectangle(x1, y1, x2, y2, fill="#BEAFC2")
    # Update x-coordinate for the next rectangle
    x1 = x2 + spacing

#clock

clock = Label(root,font=("Helvetica",30,'bold'),fg='white',bg="#747474")
clock.place(x=30,y=20)

#timezone

timezone=Label(root,font=("Helvetica",20),fg="white",bg="#747474")
timezone.place(x=600,y=20)

#long_lat = Label (root,font=("Helvetica",20),fg="white",bg="#747474")
#long_lat.place(x=600,y=50)



mainloop()
