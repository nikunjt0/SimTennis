#!/usr/bin/python3



# Imports the required libraries 
#PIL for image and tkinter for click tracker
from PIL import Image
from tkinter import *
from tkinter import ttk
from random import *
import tkinter as tk


# Create an instance of tkinter frame or window
win=Tk()

# Set the title of the window
win.title('simTennis')



# Set the size of the window
win.geometry("900x500")

# Set the global variables
count = 0
previousCoordx = 0
previousCoordy = 0

# Define a function to draw the line between two points
def draw_line(event):
   global count
   global previousCoordx
   global previousCoordy
   global lines
   x1=event.x
   y1=event.y
   x2=event.x
   y2=event.y
   # Draw an oval in the given co-ordinates
   ball = canvas.create_oval(x1,y1,x2,y2, fill="green", width=20, outline="green")
   # Make sure that the first ball doesn't make a line
   if(count > 0):
      lines = canvas.create_line(previousCoordx, previousCoordy, x1, y1,fill="red")
      canvas.after(2000, canvas.delete, lines)
   # Deletes the ball after 2 seconds   
   canvas.after(2000, canvas.delete, ball)
   # Sets the variables to be used for the next ball and line
   previousCoordx = x1
   previousCoordy = y1
   count = count + 1

# Delete line method
def delete_line():
   canvas.delete("all")
   global count
   global previousCoordx
   global previousCoordy
   previousCoordx = 0
   previousCoordy = 0
   count = 0
   canvas.create_image(100,20, anchor=NW, image=img)
   canvas.create_window(50, 200, window=player1Name)
   canvas.create_window(750, 200, window=player2Name)

# Delete lines and balls Button
refreshButton = Button(win, text="Refresh", background="black", foreground = "gray", command = delete_line)
refreshButton.grid(row = 2, column = 0)


img = PhotoImage(file="/Users/nikunjtyagi/Downloads/tennis court.gif")   
# Create a canvas widget
canvas=Canvas(win, width=700, height=400, background="white")
canvas.grid(row=0, column=0)
canvas.bind('<Button-1>', draw_line)
canvas.create_image(100,20, anchor=NW, image=img)

# player entry text box left
player1Name = tk.Entry(win, width = 10) 
canvas.create_window(50, 200, window=player1Name)

# player entry text box right
player2Name = tk.Entry(win, width = 10) 
canvas.create_window(750, 200, window=player2Name)

win.mainloop()

