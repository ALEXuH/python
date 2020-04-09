import time as _time
import threading  as _threading

'''
多线程
'''

def loop():
    print("Thread %s is running ..." % _threading.current_thread().name)
    n  = 0 
    while n < 5:
        n += 1
        print("Threading %s >>> %s" % (_threading.current_thread().name, n))
        _time.sleep(1)
    print("Thread %s is End ..." % _threading.current_thread().name)



print("Thread %s is running ..." % _threading.current_thread().name)
t1 = _threading.Thread(target=loop, name="loop")
t1.start()
t1.join()
print("Thread %s is End ..." % _threading.current_thread().name)