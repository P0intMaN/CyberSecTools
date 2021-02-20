import requests
from progress.spinner import PixelSpinner
from tqdm import tqdm
import time


class Snype:
    def __init__(self):
        self.url = input("Enter the url [without https:// or http://    (example: google.com)]  --->  ")
        print('\n')
        self.domainlist=[]
        #self.mode = int(input('Enter the mode : 1. Light Scan  ||  2. Heavy Scan (Takes a hell lot of time) --->  '))
        print('\n')
    def execute(self):
        self.file = 'subdomains.txt'
        self.f = open(self.file,'r')
        self.wordlist = self.f.read()
        self.subdomains = self.wordlist.splitlines() 
        i=0
        j=0
        print('Loading the essentials:')
        for l in tqdm(range(int(1e6)),unit='packages'):
            pass
        print('')
        time.sleep(2)
        for subdomain in self.subdomains:
            self.finalurl = f'http://{subdomain}.{self.url}'
            i+=1
            Sub = '\u001b[32mSubdomains Tried: '+ str(i).rjust(4)+"\u001b[0m"+'                    \u001b[31mFound: '+ str(j).rjust(4)+"\u001b[0m"
            print(Sub,end='',flush=True)
            print('\b'*len(Sub),end='',flush=True)
            try:
                requests.get(self.finalurl)
            except:
                pass
            else:
                j+=1
                self.domainlist.append(self.finalurl)
                 

    def result(self):
        i=0
        print("\n")
        print("\u001b[33mDiscovered URLs:\n\u001b[0m")
        for i in range(len(self.domainlist)):
            print(self.domainlist[i])
            print('')
        print('\n')
        

    

def poster():
    print( ''' 
                                             \u001b[31mSUBDOMAIN ENUMERATOR\u001b[m\u001b[33m


                                ███████╗███╗   ██╗██╗   ██╗██████╗ ███████╗
                                ██╔════╝████╗  ██║╚██╗ ██╔╝██╔══██╗██╔════╝
                                ███████╗██╔██╗ ██║ ╚████╔╝ ██████╔╝█████╗  
                                ╚════██║██║╚██╗██║  ╚██╔╝  ██╔═══╝ ██╔══╝  
                                ███████║██║ ╚████║   ██║   ██║     ███████╗
                                \u001b[31m╚══════╝╚═╝  ╚═══╝   \u001b[32m╚═╝   ╚═╝     ╚══════╝\u001b[0m
                                                                 version 1.2 \u001b[0m

                                                      \u001b[32m Developed by:\u001b[33m'THE P0intMaN'\u001b[0m
                                        
                                                    
                       \u001b[34mTo know more about Snype, visit www.github.com/P0intMaN/Snype\u001b[0m 
                       
                       
                                                                    \u001b[0m    ''')



poster()
snype = Snype()
snype.execute()
snype.result()


