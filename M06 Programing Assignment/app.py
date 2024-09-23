import time

def date_write():
    f = open("today.txt", "w")
    fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
    local = time.localtime()
    print(time.strftime(fmt, local), file = f)
    f.close

def date_read():
    f = open("today.txt", "r")
    today_string = (f.read())
    print(today_string)
    f.close

date_write()
date_read()