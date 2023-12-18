import os
import subprocess as sp
import time

class color:
    lightblue='\033[1;34m' #light blue
    lightred='\033[1;31m' #light red
    lightgreen='\033[1;32m' #lightgreen
    red='\033[0;31m' #red
    yellow='\033[1;33m' #yellow
    none='\033[0m' #no color
    purple='\033[1;35m' #purple
    cyan='\033[0;36m' #cyan
    green='\033[0;32m' #green


def help():
    print ("interface_troubleshoot - runs the interface troubleshooter, may help you locate a wireless interface or fix a problem with a known interface")
    time.sleep(1)
    devterm()
    
def search_int():
    os.system("sudo bash scrp/devterm/scrp/search_int.sh")

def missing_int():
    os.system("sudo bash scrp/devterm/scrp/missing_int.sh")

def wifi_int():
    os.system("sudo bash scrp/devterm/scrp/wifi_int.sh")

def bugged_int():
    os.system("sudo bash scrp/devterm/scrp/bugged_int.sh")

def interface_troubleshoot():
    os.system('cls' if os.name == 'nt' else 'clear')
    print ("Select an option that best applies to your issue:\n")
    print ("[1] My interface does not show on Eclipse")
    print ("[2] My interface is missing from my computer")
    print ("[3] My interface mode caused wifi to turn off")
    print ("[4] My interface does not work with Eclipse programs\n")

    select = input ("Select: ")

    if select == "1":
        search_int()
    elif select == "2":
        missing_int()
    elif select == "3":
        wifi_int()
    elif select == "4":
        bugged_int()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please Select a Valid option")
        interface_troubleshoot()

    devterm()

def devterm():
    term = input (color.green+"system@cora"+color.none+": ")
    termlow = term.lower()

    if termlow == "help":
        help()
    elif termlow == "interface_troubleshoot":
        interface_troubleshoot()
    elif termlow == "clear":
        clear()

def start():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("For a list of Commands type Help")
    devterm()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    devterm()

start()
