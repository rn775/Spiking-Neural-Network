#!/usr/local/bin/python3
# have spikes when rat is in a certain place cell

import buildCanvas
import time
from time import gmtime, strftime
#global cell0, cell1, cell2, cell3
isRunning = True
placeCell0=True
placeCell1=True
placeCell2=True
placeCell3=True

def cell_0():
    global cell0
    print(buildCanvas.coordinates, strftime("%H:%M:%S", gmtime()))
    #cell0 = False
    if(buildCanvas.coordinates[0]>50 and buildCanvas.coordinates[0]<150):
        #print("CELL 0", cell0)
        cell0 = True
        print("cell0:", cell0)
    else:
        cell0 = False
        print("cell0:", cell0)

def cell_1():
    global cell1
    #cell1 = False
    if(buildCanvas.coordinates[0]>150 and buildCanvas.coordinates[0]<250):
        #print("CELL 1", cell1)
        cell1 = True
        print("cell1:", cell1)
    else:
        cell1 = False
        print("cell1:", cell1)

def cell_2():
    global cell2
    if(buildCanvas.coordinates[0]>250 and buildCanvas.coordinates[0]<350):
        #print("CELL 2", cell2)
        cell2 = True
        print("cell2:", cell2)
    else:
        cell2 = False
        print("cell2:", cell2)

def cell_3():
    global cell3
    if(buildCanvas.coordinates[0]>350 and buildCanvas.coordinates[0]<450):
        #print("CELL 3", cell3)
        cell3 = True
        print("cell3:", cell3)
    else:
        cell3 = False
        print("cell3:", cell3)

def instantiateValues():
    global placeCell0, placeCell1, placeCell2, placeCell3
    cell_0()
    cell_1()
    cell_2()
    cell_3()
    if isRunning==True:
        if cell0==True:
            placeCell0=True
        elif cell0==False:
            placeCell0=False

        if cell1==True:
            placeCell1=True
        elif cell1==False:
            placeCell1=False

        if cell2==True:
            placeCell2=True
        elif cell2==False:
            placeCell2=False

        if cell3==True:
            placeCell3=True
        elif cell3==False:
            placeCell3=False

def run_Maze():
    global isRunning
    isRunning = True
    buildCanvas.moveImage()
    instantiateValues()

def createtheBackground():
    buildCanvas.createBackground()

def other():
    buildCanvas.others()

# made from the above 3 functions
def runMaze():
    createtheBackground()
    timeout_start = time.time()
    timeout = 5 #seconds
    while time.time() < timeout_start + timeout:
        run_Maze()
        print("Running?:", isRunning)
        print(cell0, cell1, cell2, cell3)
        #print("!!!!!!!!!!!!", placeCell0, placeCell1, placeCell2, placeCell3)
    other()

#runMaze()
