"""
进程池 回调函数
回调函数会把任务函数的结果作为参数执行
"""
from multiprocessing import Pool
import time, os

def work():
    time.sleep(1)
    print("%d 进程 work"%os.getpid())
    return time.time()
def call(res):
    print("处理回调结果：{}".format(str(res)))

if __name__ == '__main__':
    pool = Pool(2)
    for i in range(5):
        res = pool.apply_async(func=work, callback=call)
    pool.close()
    pool.join()
    print('main end')