#GUI using thread
from tkinter import *
import time
from threading import *

root = Tk()

root.geometry("400x400")

def threading():
    # Call work function
    t1 = Thread(target=work)
    t1.start()

def work():
    print("sleep time start")

    for i in range(10):
        print(i)
        time.sleep(1)

    print("sleep time stop")

Button(root, text="Click Me", command=threading).pack()
root.mainloop()