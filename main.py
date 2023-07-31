import queue
import time
from queue import Queue
import threading
q = Queue()
def fun(index):
    q.put(index)
def get():
    c = q.get()
    print(c)


from concurrent.futures import ThreadPoolExecutor

theard_pool = ThreadPoolExecutor(max_workers=2)
for i in range(1000):
    theard_pool.submit(fun, i)
thrd = ThreadPoolExecutor(max_workers = 5)
for i in range(1000):
    thrd.submit(get)
theard_pool.shutdown(wait=True)
thrd.shutdown(wait=True)