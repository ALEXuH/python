import time as _time
import threading  as _threading
from time import sleep

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



# 开启多线程方法1:直接使用初始话函数 2:继承_threading.Thread 重写run方法
print("Thread %s is running ..." % _threading.current_thread().name)
t1 = _threading.Thread(target=loop, name="loop")
t2 = _threading.Thread(target=loop, name="loop2")
t3 = _threading.Thread(target=loop, name="loop333333")
t1.start()
t2.start()
# 优先让该方法的调用者使用 CPU 资源 ，给定参数s，指定 thread 线程最多可以霸占 CPU 资源的时间（以秒为单位），如果省略，则默认直到 thread 执行结束（进入死亡状态）才释放 CPU 资源
t1.join()
t2.join(1)

# 设置为守护进程:主线程结束该进程也随之结束
t3.daemon = True
t3.start()
_time.sleep(3)

print("Thread %s is End ..." % _threading.current_thread().name)


# 线程池

# 进程池