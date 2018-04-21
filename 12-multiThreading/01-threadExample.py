"""
start_new_thread starts a program and leaves
"""


from _thread import start_new_thread
import time

def printRange(list, t):
    for element in list:
        print(element, "in thread : ", t, '\n')
        time.sleep(t)

start_new_thread(printRange,([10, 20, 30, 40, 50],2))
start_new_thread(printRange,(['a', 'b', 'c'],5))


input("")