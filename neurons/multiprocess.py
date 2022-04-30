#!/usr/local/bin/python3
import multiprocessing
import time

# run both runMaze and placeCellsSNN file at the same time
def maze(cell0, cell1, cell2, cell3):
    import placeCells
    placeCells.runMaze
    cell0.Value = cell0

#change value in SNN --> TEST
def snn(cell0, cell1, cell2, cell3):
    import placeCellsSNN
    if cell0.Value==True:
        G.run_regularly('selected_index = 1', dt=20*ms, when='end')

if __name__ == '__main__':

    #timestep

    cell0 = Value('d', 0.0)
    #cell1 = Value('d', 0.0)
    #cell2 = Value('d', 0.0)
    #cell3 = Value('d', 0.0)

    p1 = Process(target=maze, args=[cell0])
    p2 = Process(target=snn, args=[cell0])

    p1 = multiprocessing.Process(target=maze)
    p2 = multiprocessing.Process(target=snn)
    p1.start()
    #time.sleep(0.1)
    p2.start()
    p1.join()
    p2.join()

'''

'''
