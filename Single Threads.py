import threading
import time

def simlpe_thread():
    print(" Program Runs Successfully")


t = threading.Thread(target=simlpe_thread)
t.start()
t.join()
