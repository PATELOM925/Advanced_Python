import threading
import time

shared_res = 0 #variable that will be shared btwn 2 threads
lock = threading.Lock() #it's an instance opf threading.lock class
#this lock synchronizes access to shared resource

def in_resource():
    global shared_res
    for _ in range(5):
        with lock:
            shared_res += 1
            print(f' Incremented = {shared_res} ')
        time.sleep(1)
      

def dec_resource():
    global shared_res
    for _ in range(5):
        with lock:
            shared_res -= 1
            print(f' Decremented = {shared_res} ')
        time.sleep(1)
        
if __name__ == '__main__':
    thread1 = threading.Thread(target=in_resource)
    thread2 = threading.Thread(target=dec_resource)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print("Thread Task Completed")
           
                      