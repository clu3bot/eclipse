import os 
import time
import subprocess as sp

global intname

intname = sp.getoutput("sudo python3 scrp/inthandler/rename.py")

global networkname

networkname = sp.getoutput("")


def blacklistmode():

def whitelistmode():

def allmode():

def menu():
    print ("Currently Selected Network:"+networkname+"\n\n")

    print ("Deauth Options:\n")
    print ("[1] Blacklist Mode")
    print ("[2] Whitelist Mode")
    print ("[3] Deauth All Devices")

    userchoice = input ("\nSelect an Option: ")

    if int(userchoice) == 1:
        blacklistmode()
    elif int(userchoice) == 2:
        whitelistmode()
    elif int(userchoice) == 3:
        allmode()
    else:
        print ("Invalid selection. Select again..")
        time.sleep(3)
        menu()

