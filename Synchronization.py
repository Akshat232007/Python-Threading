import threading as t

counter = 0
lock = t.Lock()

def count(arg):
    global counter
    for i in range(10):
        with lock:
            counter += 1

t1 = t.Thread(target=count, args=("A",))
t2 = t.Thread(target=count, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Final Counter : {counter}")
