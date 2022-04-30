#!/usr/local/bin/python3
from multiprocessing import Process, Value, Array
import time

'''
# run both runMaze and placeCellsSNN file at the same time
def a(count):
    for x in range (0,10):
        count.value+=1

def b(count):
    for x in range (0,10):
        print("COUNT: ", count.value)

if __name__ == '__main__':
    num = Value('d', 0.0)
    p1 = Process(target=a, args=[num])
    p2 = Process(target=b, args=[num])
    p1.start()
    p2.start()
    p1.join()
    p2.join()
'''

from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
