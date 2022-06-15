"""
进程间通信——--队列
IPC (Inter-Process Communication)
特点： 先进先出
Queue([maxsize])
创建共享的进程队列
参数； maxsize 是队列中允许的最大项数。如果省略，则无大小限制
q.get([block [,timeout]])
返回q中的一个项目。如果q为空，此方法将阻塞，直到队列中有项目可用为止。block用于控制阻塞行
为，默认为True. 如果设置为False，将引发Queue.Empty异常（定义在Queue模块中）。timeout是
可选超时时间，用在阻塞模式中。如果在制定的时间间隔内没有项目变为可用，将引发Queue.Empty
异常。
q.get_nowait() == q.get(False)
q.put(item [, block[, timeout]]
将item放入队列。如果队列已满，此方法将阻塞至有空间可用为止。block控制阻塞行为，默认为
True。如果设置为False，将引发Queue.Empty异常（定义在Queue库模块中）。timeout指定在阻
塞模式中等待可用空间的时间长短。超时后将引发Queue.Full异常。

q.qsize(0 返回正确数量
q.empty() 为空 返回 True
q.full() 已满 返回True
"""
import os
import random
import time
from multiprocessing import Process, Queue, JoinableQueue
def f(q):
    q.put([time.asctime(), 'from SX', 'hello'])

def consunmer1(q):
    while True:
        res = q.get() # 在q为空时，进程进入阻塞状态，而此时生产者已经停止了
        if res =='完成': # 生产者完成后发送结束信号 完成
            break
        time.sleep(random.randint(1, 3))
        print('\033[45m%s 吃了 %s\033[0m'%(os.getpid(), res))
def producer1(q):
    for i in range(10):
        time.sleep(random.randint(1, 3))
        res = '包子%s'%i
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m'%(os.getpid(), res))
    q.put('完成')

# joinableQueue
def consumer2(q):
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print('\033[45m%s 吃了 %s\033[0m'%(os.getpid(), res))
        q.task_done() # 向q.join() 发送一次信号
def producer2(q):
    for i in range(10):
        time.sleep(random.randint(1, 3))
        res = '包子%s'%i
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m'%(os.getpid(), res))
        q.join()
if __name__ == '__main__':
    q = JoinableQueue()
    # 生产者
    p1 = Process(target=producer1, args=(q, ))
    # 消费者
    c1 = Process(target=consunmer1, args=(q, ))

    # 开始
    p1.start()
    c1.start()
    print('主 线程')