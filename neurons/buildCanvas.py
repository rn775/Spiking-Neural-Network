#!/usr/local/bin/python3
from tkinter import *
from PIL import ImageTk, Image
import time
import random

global coordinates
global xVel
global yVel
global c
global root
xVel = 20
yVel = 20



def createCanvas():
    global c
    global root
    root = Tk()
    c = Canvas(root, bg="white",height=600, width=600)
    root.title('GUI for SNN')
    # initialise canvas
    #c = Canvas(root, bg="white",height=600, width=600)
    # extend window size when window is stretched
    c.pack(fill="both", expand=True)

# draw the grid
def createGrid():
    c.create_line(100, 100, 500, 100, fill="grey", width=2)
    c.create_line(100, 100, 100, 500, fill="grey", width=2)
    c.create_line(100, 500, 500, 500, fill="grey", width=2)
    c.create_line(500, 500, 500, 100, fill="grey", width=2)

    for i in range (4):
        c.create_line(100, 100+100*i, 500, 100+100*i, fill="grey", width=2)

    for i in range (4):
        c.create_line(100+100*i, 100, 100+100*i, 500, fill="grey", width=2)

# add text of each cell number for reference
def addCellNumber():
    for i in range (4):
        for j in range (4):
            c.create_text(150+(100*i), 150+(100*j), text=i+4*j, fill="light grey", font=('Helvetica 30 bold'))

# insert image of subject to move
def insertImage():
    global img
    global mouse
    mousePic = "/Users/rabia/github/SNN/Neuron/mousie.png"
    # open and resize the picture
    img = ImageTk.PhotoImage(Image.open(mousePic).resize((100,80), Image.ANTIALIAS))
    mouse = c.create_image(100, 100, anchor=NW, image=img)
    #mouse_width = mouse.width()
    #mouse_height = mouse.height()

# move subject around RANDOM
def moveImage():
    global xVel
    global yVel
    global coordinates
    coordinates = c.coords(mouse)
    if(coordinates[0]>400 or coordinates[0]<100):
        xVel = -xVel
    if(coordinates[1]>400 or coordinates[1]<100):
        yVel = -yVel
    c.move(mouse, xVel, 0)
    root.update()
    time.sleep(0.02)

def createBackground():
    createCanvas()
    createGrid()
    addCellNumber()
    insertImage()

#while True:
    #moveImage()
def others():
    root.mainloop()
    root.update()
    c.show()
