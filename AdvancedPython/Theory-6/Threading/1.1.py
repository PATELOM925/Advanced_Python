#imp to write start and then join function
#start fucntion will itself call the run function
#join is written to block our main thread untill and unless all our threads gets executed
#if join not written main thread will run

import threading
import time

lock = threading.Lock()

def task1():
    for i in range (5):
        with lock:
            print(f"{i} Task 1 has been executed ")
            time.sleep(1)
        
def task2():
    with lock:
        for i in range(5):
            print(f"{i} Task 2 completed")
            time.sleep(1)
        
if __name__ == "__main__":
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    print("All Task have been excecuted")
                    
    
    