import multiprocessing
import time
import os
import random

def whoami(name):
    print("I'm %s, in process %s" % (name, os.getpid()))

def pro1():
    wait = random.random()
    time.sleep(wait)
    name = "Process 1"
    whoami(name)
    local = time.localtime()
    print(time.strftime(fmt, local))

def pro2():
    wait = random.random()
    time.sleep(wait)
    name = "Process 2"
    whoami(name)
    local = time.localtime()
    print(time.strftime(fmt, local))

def pro3():
    wait = random.random()
    time.sleep(wait)
    name = "Process 3"
    whoami(name)
    local = time.localtime()
    print(time.strftime(fmt, local))

if __name__ == "__main__":
    fmt = "    It's %A, %B %d, %Y, local time %I:%M:%S%p"
    pro1()
    pro2()
    pro3()
    p = multiprocessing.Process(target=pro1, args=("Process 1"))
    p = multiprocessing.Process(target=pro2, args=("Process 2",))
    p = multiprocessing.Process(target=pro3, args=("Process 3",))
