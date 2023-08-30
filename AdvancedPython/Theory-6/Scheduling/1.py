#Example - code for schedule library 
#using "every" commands for custom seconds and define time
import schedule
import time
import datetime

import schedule
import time
import datetime

def task1():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] Task 1 executed!")

def task2():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] Task 2 executed!!")

def task3():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] Task 3 executed!!!")

if __name__ == "__main__":
    # scheduling task 1 for every 2 seconds
    schedule.every(2).seconds.do(task1)
    
    # scheduling task 2 for every 5 seconds
    schedule.every(5).seconds.do(task2)
    

    while True:
        schedule.run_pending()
        time.sleep(1)
