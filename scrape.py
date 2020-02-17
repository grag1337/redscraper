from bs4 import BeautifulSoup
from os import system, name
from time import sleep
from subprocess import call
import urllib
import socket
import requests
from urllib.request import Request, urlopen
from art import *
import re
import keyboard
import os

try:
    def clear():
        if name == "nt":
            system('cls')
        else:
            system("clear")

    def getLink():
        clear()
        print("[+] e.g r/ambien ; r/pics")
        url = input("[*] What subreddit do you want to scrape? \n [*] \n : ")
        url2 = "https://www.reddit.com/" + url
        print("[+] Your url is " + url2 + ", is this correct? (Y, N)")
        yesno = input("[*] \n : ")
        if yesno == ("Y" or "y"):
            clear()
            print("coo")
            sleep(2)
            print()
            download_image(url2)
        elif yesno == ("N" or "n"):
            clear()
            print("not coo")
            sleep(2)
            getLink()

    def download_image(url):
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                       'Accept-Encoding': 'none',
                       'Accept-Language': 'en-US,en;q=0.8',
                       'Connection': 'keep-alive'}
        req = Request(url, headers=hdr)
        page = urlopen(req).read()
        soup = BeautifulSoup(page, "html.parser")
        soup2 = soup.findAll(alt="Post image")
        print([i.find('img')['src'] for i in soup2])

        
        #resp = requests.get(url, stream=True)
        #local_file = open('local_image.jpg', 'wb')
        #resp.raw.decode_content = True
        #shutil.copyfileobj(resp.raw, local_file)

    getLink()

except KeyboardInterrupt:
    clear() 
    print("Exiting..")
    sleep(2)
    clear()
    exit

#except:
#    clear()
#    print("An unexpected error has occured...")
    
