import socket
import os
import sys
import time
from queue import Queue
import threading
from progress.bar import ShadyBar



queue = Queue()
portslist = range(1, 1024)
threadslist = []
portsresult = []
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def banner():
    print('''\u001b[92m 
    
                    ██████╗ ███████╗██╗     ██╗ ██████╗ █████╗ ███╗   ██╗
                    ██╔══██╗██╔════╝██║     ██║██╔════╝██╔══██╗████╗  ██║ 
                    ██████╔╝█████╗  ██║     ██║██║     ███████║██╔██╗ ██║ 
                    ██╔═══╝ ██╔══╝  ██║     ██║██║     ██╔══██║██║╚██╗██║
                    ██║     ███████╗███████╗██║╚██████╗██║  ██║██║ ╚████║ \u001b[32mPORT SCANNER TOOL
                 \u001b[31m   ╚═╝     ╚══════╝╚══════╝╚═╝ ╚═════╝\u001b[33m╚═╝  ╚═╝╚═╝  ╚═══╝    \u001b[36m version 1.1.4\u001b[0m
                                      \u001b[31mDeveloped by:\u001b[33m'THE P0intMaN'\u001b[0m


                       \u001b[34mTo know more about Pelican, visit www.github.com/P0intMaN/Pelican\u001b[0m       
      ''')


def error():
    print("\u001b[91mInvalid Input!!  Quitting the Interface...\u001b[0m")
    sys.exit(1)

def openports():
    print("\n\u001b[36mThe Open Ports are -->\u001b[0m ", portsresult)

def intro():
    print("\n\n\u001b[33m------ INITIALISING PELICAN INTERFACE ------\u001b[0m\n")
    time.sleep(3)

def end():
    print("\n\n\u001b[33m------ PORT SCAN SUCCESSFULLY COMPLETED ------\u001b[0m")
    time.sleep(2)
    

def portscan():
    print("\n\n\u001b[33m------ INITIALSING PORT SCAN INTERFACE ------\u001b[0m\n")
    mylist = {80, 25, 22, 540, 443, 444, 432, 20, 0, 1, 54, 6000, 5690, 1024, 664, 78, 8897, 897, 87, 65, 654, 65656, 7865}
    shady = ShadyBar('\u001b[31mPreparing to Scan... \u001b[0m ', max = len(mylist))
    for i in mylist:
        shady.next()
        time.sleep(0.1)
    print('\n\n')


os.system('cls')
banner()
intro()

try:
    prompt = int(input("\n\u001b[36mChoose the Method of Input  \u001b[92m( 1: Enter the website || 2: Enter the IP adress ) \u001b[36m-->\u001b[0m "))
    if prompt > 2:
        print("\u001b[91mINVALID ENTRY!\u001b[0m ")
        sys.exit(1)
except:
    error()
    
if prompt == int(1):
    try:
        host = input("\n\u001b[36mEnter the Website -->\u001b[0m ")
        print("\n\n\u001b[33m------ CHECKING YOUR INPUT ------\u001b[0m")
        time.sleep(2)
        ip = socket.gethostbyname(host)
        print("\n\u001b[32mYour Input is \u001b[33mValid!\u001b[32m The IP Adress of {} is : \u001b[31m{} \u001b[0m----> Additional info :)\u001b[0m".format(host, ip))
        time.sleep(1)
        print("\u001b[32mRedirecting to the Interface...\u001b[0m")
    except:
        error()

if prompt == int(2):
        ip = input("\n\u001b[36mEnter the IP Adress -->\u001b[0m ")
        print("\n\n\u001b[33m------ CHECKING YOUR INPUT ------\u001b[0m")
        time.sleep(2)
        checkresult = os.system('ping -n 4 {}'.format(ip))
        if checkresult == 0:
            print("\n\u001b[32mYour Input is \u001b[33mValid! \u001b[32mRedirecting to the Interface...\u001b[0m")
            time.sleep(3)
        else:
            error()
        
try:
    method = int(input("\n\u001b[36mEnter the Scanning Method //>\u001b[32m  1: MANUAL SCAN  2: AUTOMATIC SCAN\u001b[0m \u001b[36m-->\u001b[0m "))
    if method >2:
        error()
except:
    error()

if method == 1:
    try:
        port = int(input("\u001b[36mEnter the Port -->\u001b[0m ")) 
    except:
        error()
    try:
        portscan()
        a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if a.connect((ip,port)) !=0:
            print("\u001b[32mPort\u001b[0m {}\u001b[32m Status is: OPEN\u001b[0m".format(port))     
    except:
        print("\u001b[31mPort \u001b[0m{}\u001b[31m Status is: CLOSED\u001b[0m".format(port))
    end()
    time.sleep(5)
    sys.exit(0)

if method == 2:
    portscan()

    def scan(port):
        try:
            a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            a.connect((ip,port))
            return True
        except:
            return False

    def insertqueue(portslist):
        for i in portslist:
            queue.put(i)

    def worker():
        while not queue.empty():
            port = queue.get()
            if scan(port):
                print("\u001b[32mPort \u001b[0m{}\u001b[32m  Status is: OPEN\u001b[0m ".format(port) )
                portsresult.append(port)
            else:
                print("\u001b[31mPort \u001b[0m{}\u001b[31m Status is: CLOSED\u001b[0m".format(port))                   


    insertqueue(portslist)

    for j in range(800):
        threads = threading.Thread(target = worker)
        threadslist.append(threads)

    for threads in threadslist:
        threads.start()

    for threads in threadslist:
        threads.join()

    end()
    openports()
    time.sleep(15)
    sys.exit(0)
    
