#!/usr/local/bin/python3
import placeCells

#Record true false values
placeCell1=False
placeCell2=False
placeCell3=False
placeCell4=False
def values():
    global placeCell1, placeCell2, placeCell3, placeCell4
    if placeCells.isRunning==True:
        if placeCells.cell0==True:
            placeCell1=True
        elif placeCells.cell0==False:
            placeCell1=False

        if placeCells.cell1==True:
            placeCell2=True
        elif placeCells.cell1==False:
            placeCell2=False

        if placeCells.cell2==True:
                placeCell3=True
        elif placeCells.cell2==False:
            placeCell3=False

        if placeCells.cell3==True:
            placeCell4=True
        elif placeCells.cell3==False:
            placeCell4=False

def printValues():
    global placeCell1, placeCell2, placeCell3, placeCell4
    print('!!!!!!!!!!!Place1:', placeCell1,' Place2:', placeCell2,' Place3:', placeCell3,' Place4:', placeCell4)
