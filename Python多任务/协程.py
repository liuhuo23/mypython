"""
进程是资源分配的最小单位
线程是CPU调度的最小单位
引入协程的原因： 频繁的切换线程会非常消耗性能，而协程的切换只是单纯的操作CPU的上下文

协程的本质就是在单线程下，由用户自己控制一个任务遇到io阻塞就切换另外一个任务去执行一次来提升效率
实现协程的两个要素
1. 可以控制多个任务之间的切换，切换之前将任务的状态保存下来，以便重新运行时，可以基于暂停的位置继续执行
2。 作为1的补充，可以检测io操作，在遇到io操作的情况下才发生切换

协程介绍
协程：单线程下的并发，又称微线程 协程一种用户态的轻量级线程，即协程是由用户程序自己控制调度的
Python的线程属于内核级别的，即由操作系统控制调度
单线程内开启协程，一旦遇到io，就会从应用程序级别（非操作系统）控制切换，以此来提升效率
优点：
协程的切换开销小
单线程内就可以实现并发的效果，最大限度的利用CPU
缺点：
本质是单线程无法利用多核，可以是一个线程开启多个进程，每个进程内开启多个线程，每个线程内开启协程
协程指的是单个线程，因而一旦协程出现阻塞，将会阻塞整个线程

Gevnet 模块
pip install gevent
"""
import random
import time

"""
g1 = gevent.spawn(func, 1,2,3,x=4,y=5)创建一个协程对象g1 spawn 括号内第一个参数是函数名
g2 = gevent.spawn(func2)
g1.join() 等待g1结束
g2.join() 等待g2结束
g1.value 拿到func1的返回值
"""

import gevent
from gevent import  monkey
monkey.patch_all() # 将程序左手拿个用到的耗时操作的代码，换位gevent中自己实现的模块


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # 用来模拟一个耗时操作
        gevent.sleep(1)

def work(name):
    for i in range(10):
        print(name, i)
        time.sleep(random.random())

if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(work, 'wokr1'),
        gevent.spawn(work, 'work2')
    ])
