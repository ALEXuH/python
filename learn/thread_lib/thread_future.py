#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Author : ALEXuH
# @Created on : 2020/12/26 16:05

from concurrent import futures


def printer(n):
    # _time.sleep(n)
    # print("sleep {}s output {}".format(n, n))
    return n*n


if __name__ == '__main__':

    # 创建线程池获取结果 map
    #executor = futures.ThreadPoolExecutor(max_workers=4)
    # results = executor.map(printer, [4, 1, 2, 3, 0])
    # for i, result in enumerate(results):
    #     print("result: %s %s" %(i, result))

    # submit方式as_completed
    # submit_result = {executor.submit(printer, [4, 3, 1, 0, 5], 60)}
    # print(submit_result)

    # submit 方式
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_result = {executor.submit(printer, i): i for i in [1, 2, 3, 4, 5]}
        print(futures)
        for future in futures.as_completed(future_result):
            try:
                print(future)
                print(future.result())
            except Exception as e:
                print(e)



