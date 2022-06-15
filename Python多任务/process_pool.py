"""
创建进程需要消耗时间，销毁进程也需要消耗时间
即便开启多个线程，操作系统也不会让他们同时执行
进程池的概念：
一开始就创建多个进程，将进程与任务分开。
Pool([numprocess[, initializer [, initargs]]]) 创建进程池
参数：
1. numprocess 要创建的进程数，入宫神略，将默认使用 cpu_count()的值
2. initalizer 是每一个工作进程启动时要执行的可调用对象，默认为None
3. initargs 是要床给initializer的参数组
p.applay(func[,args[,kwargs]]) 在一个池工作进程中执行func(*args, **kwargs)然后返回结果 。 同步
p.applay_async(func [, args [,kwargs]]) 异步
p.close() 关闭进程池
p.join()等地啊所有工作进程退出。此方法只能在close(0 或 terminate()之后调用

"""
import os,time
from multiprocessing import Pool
# 进程池的同步调用
def work(n):
    print('%s run'% os.getpid())
    time.sleep(3)
    return n**2

if __name__ == '__main__':
    p = Pool(3)
    res_1 = []
    for i in range(10):
        # res = p.apply(work, args=(i,))
        # res_1.append(res)
        # 异步调用
        res = p.apply_async(work, args=(i, )) # 异步运行
        res_1.append(res)
    p.close()
    p.join()
    for res in res_1:
        print(res.get())
