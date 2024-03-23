from tkinter import *
import tkinter as tk
from getINFO import getWeather

# Create a window
root = Tk()
root.title("Look, the Weather!")
root.geometry("890x470+300+300")  # The format is width x height + x_offset + y_offset
root.configure(bg="#747474")
root.resizable(False, False)  # Window not resizable

# Calculate the center coordinates of the window
window_center_x = root.winfo_reqwidth() // 2
window_center_y = root.winfo_reqheight() // 2


Label(root, bg="#707070").place(x=100, y=110)

weather_labels = []  # List to store label widgets for weather information
LabelAux = Label(root,text = None, font=("Arial", 17), bg="#747474")
LabelAux.place(x=window_center_x, y=250)
weather_labels.append(LabelAux)
#LabelAux.grid_remove()  #  it is hided first 

for idx in range(4):
    label = Label(root,text = None, font=("Arial", 15), bg="#747474")
    label.place(x=window_center_x, y=300 + (idx * 30))
    weather_labels.append(label)
    #label.grid_remove() # initially hide the labels


# Label for the instruction
instruction_label = Label(root, text="Enter the city and press enter:", font=("poppins", 15), bg="#747474", fg="white")
instruction_label.place(x=window_center_x + 80, y=window_center_y)

# Search box
textfield = Entry(root, justify='center', width=30, font=("poppins", 25, 'bold'), bg="#444444", border=0)
textfield.place(x=window_center_x +80 , y=window_center_y + 40 )
textfield.focus()  # Focus by default
# Bind the Enter key to call the function
textfield.bind("<Return>", lambda event: getWeather(textfield.get(), clock, timezone,weather_labels))

#clock

clock = Label(root,font=("Helvetica",30,'bold'),fg='white',bg="#747474")
clock.place(x=30,y=20)

#timezone

timezone=Label(root,font=("Helvetica",20),fg="white",bg="#747474")
timezone.place(x=600,y=20)


mainloop()
