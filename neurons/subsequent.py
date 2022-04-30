#!/usr/local/bin/python3
import placeCells
from brian2 import *
import time
import placeCellsSNN
from time import gmtime, strftime
import multiprocessing

def maze():
    placeCells.createtheBackground()
    timeout_start = time.time()
    timeout = 5 #seconds
    while time.time() < timeout_start + timeout:
        placeCells.run_Maze()
        print(placeCells.cell0, placeCells.cell1, placeCells.cell2, placeCells.cell3)
        print("Running?:", placeCells.isRunning)
    placeCells.other()

def snn():
    if placeCells.placeCell0==True:
        placeCellsSNN.G.run_regularly('selected_index = 1', dt=20*ms, when='end')
        print("\n             neuron 1", placeCells.placeCell0, placeCells.isRunning, strftime("%H:%M:%S", gmtime()))

    if placeCells.placeCell1==True:
        placeCellsSNN.G.run_regularly('selected_index = 2', dt=20*ms, when='end')
        print("\n             neuron 2", placeCells.placeCell1, placeCells.isRunning, strftime("%H:%M:%S", gmtime()))

    if placeCells.placeCell2==True:
        placeCellsSNN.G.run_regularly('selected_index = 3', dt=20*ms, when='end')
        print("\n             neuron 3", placeCells.placeCell2, placeCells.isRunning, strftime("%H:%M:%S", gmtime()))

    if placeCells.placeCell3==True:
        placeCellsSNN.G.run_regularly('selected_index = 4', dt=20*ms, when='end')
        print("\n             neuron 4", placeCells.placeCell3, placeCells.isRunning, strftime("%H:%M:%S", gmtime()))

    placeCellsSNN.runNN()

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=maze)
    p2 = multiprocessing.Process(target=snn)
    p1.start()
    time.sleep(0.1)
    p2.start()
    p1.join()
    p2.join()
