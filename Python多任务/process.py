# multi(多)process(任务) 模块
"""
Python 慢的原因
1. 动态性语言，边解释边执行
2.  GIL 无法利用多喝GPU并发执行
全局解释器锁 （Global Interpreter Lock） 使得任何时刻仅有一个线程执行
即便再多核处理器上，使用GIL的解释器也只允许同一时刻执行一个线程
为了解决多线程之间数据完整性和状态同步问题
Python中对象的管理，是使用引用计数器进行的，引用数为0则释放对象
Process([group [,target [, name [,ages [, kwargs]]]]]), 由该类实例化得到的对象
args 指定的为传给target函数的位置参数， 是一个元组，必须有逗号
1. group参数未使用，值始终为None
2. target表示调用对象的位置参数元组，args=(1, 2, 'egon',)
3. args 表示调用对象的位置参数元组，args=(1， 2， ‘egon')
4. kwargs表示调用对象的字典，kwargs={'name':'egon'}
5. name为子进程的名称

p.start() :启动进程，并调用该子进程中的p.run()
p.run() 进程启动时运行的方法
p.terminate() 强制终止进程给p，不会进行任何清理操作，如果P创建了子进程，该子进程就成了僵尸进程
p.is_alive(0 p 正在运行返回True
p.join([timeout]) 主线程等待p终止， p.join 只能join 住start开启的进程，而不能join run开启的进程

p.daemon 默认值为False,如果设为True ,代表p为后台运行的守护进程，当p的父进程终止时，p随之终止。 设定为True，p不能创建自己的新进程
p.name 进程的名称
p.pid 进程pid
p.exitcode 进程再运行时为None，如果-N，表示信号N结束了
p.authkey 进程的身份证验证键，默认是由os.urandom() 随机生成的32字符的字符串。 主要设计网络连接的底层进程间通信提供安全性
"""
import os
import random

"""
信号量
Semaphore 
acquire() 信号量减1
release() 信号量加1
当信号量为0则阻塞
"""
"""
事件
from multiprocessing import Event
e.set()  将 is_set 设为 True
e.clear() 将 is_set 设为 False
e.wait()
e.is_set() Flase e.wait() 阻塞 True e.wait() 非阻塞
"""
import time  # 导入时间
# 导入多任务模块
from multiprocessing import Process, Semaphore

# 创建信号量对象，初始化为3
sem = Semaphore(3)


def fun(name):
    # 打印进程号
    print('进程%d等待信号量' % os.getpid())
    # 消耗一个信号量
    sem.acquire()
    print('进程%d 消耗了1个信号量' % os.getpid())
    time.sleep(random.randint(2, 5))
    sem.release()
    print('进程%d 添加了1个信号量' % os.getpid())


if __name__ == '__main__':
    jobs = []
    for i in range(4):
        p = Process(target=fun, args=('hello%d' % i,))
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()
