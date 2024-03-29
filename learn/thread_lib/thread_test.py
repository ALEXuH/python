#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading as _threading
import time

# 为线程定义一个函数
def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ("%s: %s" % (threadName, time.ctime(time.time())))

# 创建两个线程
try:
    _threading.start_new_thread(print_time, ("Thread-1", 2, ))
    _threading.start_new_thread(print_time, ("Thread-2", 4, ))
    _threading.start_new_thread(print_time, ("Thread-3", 1))
except:
    print ("Error: unable to start thread")

while 1:
    pass