import threading

def Worker_A():
    for i in range(5+1):
        print(f"Thread Worker_A : working counter {i} ")

def Worker_B():
    for i in range(5+1):
        print(f"Thread Worker_B : working counter {i} ")

t1 = threading.Thread(target=Worker_A)
t2 = threading.Thread(target=Worker_B)


t1.start()
t2.start()


t1.join()
t2.join()

print("All threads completed.")
