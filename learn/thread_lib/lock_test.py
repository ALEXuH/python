#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Author : ALEXuH
# @Created on : 2020/12/26 16:05

import threading as _threading
import time as _time
import queue

number = 0
q = queue.Queue(10)

def loop():
    print("Thread %s is running ..." % _threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print("Threading %s >>> %s" % (_threading.current_thread().name, n))
        _time.sleep(1)
    print("Thread %s is End ..." % _threading.current_thread().name)


# 互斥锁（独占），同一个时刻只能一个线程访问数据，避免同时操作数据导致脏数据
def plus(lk):
    global number
    lk.acquire()
    for i in range(1000000):
        number += 1
    print("Threading %s >>> %s" % (_threading.current_thread().name, number))
    lk.release()


def run(n, se):
    se.acquire()
    print("Threading %s >>> %s" % (_threading.current_thread().name, n))
    _time.sleep(1)
    se.release()

def produce(i):
    while True:
        print("厨师 %s 做了一个包子" % i)
        q.put("厨师 %s 做的包子" % i)
        _time.sleep(2)


def consumer(i):
    while True:
        print("顾客 %s 吃了一个 %s" % (i, q.get()))
        _time.sleep(2)


if __name__ == '__main__':
    # 互斥锁
    # lock = _threading.Lock()
    # for i in range(2):
    #     t = _threading.Thread(target=plus, args=(lock,))
    #     t.start()
    # _time.sleep(2)
    # print("number: %s" % number)

    # 信号sem 允许一定数量线程同时更改数据
    # se = _threading.BoundedSemaphore(5)
    # for i in range(20):
    #     t = _threading.Thread(target=run, args=(i, se))
    #     t.start()

    # 生产者消费者
    for i in range(50):
        t = _threading.Thread(target=produce, args=(i,))
        t.start()

    # 消费者
    for j in range(10):
        v = _threading.Thread(target=consumer, args=(j,))
        v.start()


    # 线程池

