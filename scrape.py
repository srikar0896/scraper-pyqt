import urllib
import urllib.request
from bs4 import BeautifulSoup
def scrape(url):
    try:
        if url.startswith("https://"):
            urlOpen=urllib.request.urlopen(url)
            print("------------------- "+ url +" ----------------")
            content=urlOpen.read()
            soup=BeautifulSoup(content,"html5lib")
            links=soup.find_all("a")
            f=open("11.txt","a",encoding="utf-8")
            f.write("\n---------------scraping " + url + "-------------------------\n")
            for link in links:
                text=link.text
                href=link.get("href")
                f.write(text + " --\t[" + href + "]\n")
            f.write("\n*****************Ended Scraping " + url +" ****************\n")
        elif url.startswith("/"):
            url="https://google.com" + url
            urlOpen=urllib.request.urlopen(url)
            print("------------------- "+ url +" ----------------")
            content=urlOpen.read()
            soup=BeautifulSoup(content,"html5lib")
            links=soup.find_all("a")
            f=open("10.txt","a",encoding="utf-8")
            f.write("\n---------------scraping " + url + "-------------------------\n")
            for link in links:
                text=link.text
                href=link.get("href")
                f.write(text + " --\t[" + href + "]\n")
            f.write("\n*****************Ended Scraping " + url +" ****************\n")
    except Exception:
        pass
urlOpen=urllib.request.urlopen("http://google.com/")
content=urlOpen.read()
soup=BeautifulSoup(content,"html5lib")
links=soup.find_all("a")
f=open("welcome.txt","w+",encoding="utf-8")
f=open("welcome.txt","w+",encoding="utf-8")
f.write("*********************************\n")
book={}
for link in links:
    href=link.get("href")
    text=link.text
    book[text]=href
    f.write(text + "\t--[" + href +"]\n")
for golink in book.values():
    scrape(golink)
    f.write("\n*****************Scraping" + golink +" Begins****************\n")
f.flush()
f.close()
 
