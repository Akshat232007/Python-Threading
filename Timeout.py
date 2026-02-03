import threading as t
import time as tm

lock1 = t.Lock()
lock2 = t.Lock()

def task1():
    if lock1.acquire(timeout=3):
        print("Task 1 acquired lock 1")
        tm.sleep(2)
        if lock2.acquire(timeout=3):
            print("Task 1 acquired lock 2")
            lock2.release()
        else:
            print("Task 1 could NOT acquire lock 2 (timeout)")
        lock1.release()
    else:
        print("Task 1 could NOT acquire lock 1 (timeout)")

def task2():
    if lock2.acquire(timeout=3):
        print("Task 2 acquired lock 2")
        tm.sleep(2)
        if lock1.acquire(timeout=3):
            print("Task 2 acquired lock 1")
            lock1.release()
        else:
            print("Task 2 could NOT acquire lock 1 (timeout)")
        lock2.release()
    else:
        print("Task 2 could NOT acquire lock 2 (timeout)")

t1 = t.Thread(target=task1)
t2 = t.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()
