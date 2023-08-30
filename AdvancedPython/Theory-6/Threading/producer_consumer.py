import threading
import time
import random

BUFFER_SIZE = 10

lock = threading.Lock()
buffer_not_full = threading.Condition(lock)
buffer_not_empty = threading.Condition(lock)
buffer = []

def prod():
    global buffer
    item = random.randint(28,99)
    
    with buffer_not_full:
        while len(buffer) >= BUFFER_SIZE:
            buffer_not_full.wait()
        buffer.append(item)  
        print(f" Produced {item} , buffer: {buffer}")
        buffer_not_empty.notify()
        time.sleep(random.uniform(0.3, 0.9)) 
        
def cons():
    global buffer
    while True:
        with buffer_not_empty:
            while len(buffer) == 0:
                buffer_not_empty.wait()
            item = buffer.pop(0)
            print(f" Consumed {item} , buffer: {buffer}")
            buffer_not_full.notify()
        
        time.sleep(random.uniform(0.3, 0.9))
        
if __name__ == "__main__":
    producers = 6
    consumers = 6
    
    producer_threads = [threading.Thread(target=prod) for _ in range(producers)]
    consumer_threads = [threading.Thread(target=cons) for _ in range(consumers)]
    
    for thread in producer_threads + consumer_threads:
        thread.start()
    
    for thread in producer_threads + consumer_threads:
        thread.join()