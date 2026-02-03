import threading as t
import time as tm

lock1=t.Lock()
lock2=t.Lock()

def task1():
    with lock1:
        print("Task 1 acquired by lock 1")
        tm.sleep(2)
        with lock2:
            print("Task 1 acquired by lock 2")

def task2():
    with lock2:
        print("Task 2 Acquired by lock 2")
        tm.sleep(2)
        with lock1:
            print("Task 2 Acquired by lock1")

t1=t.Thread(target=task1)
t2=t.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()
