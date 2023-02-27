import subprocess as sp
import os
import time
import platform
from os.path import exists


#colar vars
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

def permissions():  #checks for root permissions
    if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
        print(color.lightred + "You need to run this script with sudo or as root.")
        time.sleep(0.3)
        quit()

permissions()

def getos():
    osys=platform.system()
    if osys != "Linux":
        print(color.lightred + "This program only runs on Linux operating systems.")
        time.sleep(2)
        quit()

getos()


def check_file():
    file = exists("tmp/flag.txt")

    if file == 'True':
        os.system("rm -rf tmp/flag.txt")
    else:
        time.sleep(0.5)

check_file()

#dependencies
class dependencies:
    dependencie1 = 'mdk3'
    dependencie2 = 'aircrack-ng'
    dependencie3 = 'xterm'
    dependencie4 = 'macchanger'

def check_mdk3():
    
    check_d1 = sp.getoutput("bash etc/dpkg-check/dpkg-check-mdk3.sh")

    if check_d1 == '0': 
        mdk3 = 'null'
    else:
        mdk3 = 'inst'

    return mdk3

def check_aircrack():
    
    check_d2 = sp.getoutput("bash etc/dpkg-check/dpkg-check-aircrack-ng.sh")    
    
    if check_d2 == '0':
        aircrack = 'null'
    else:
        aircrack = 'inst'
    
    return aircrack

def check_xterm():
    check_d3 = sp.getoutput("bash etc/dpkg-check/dpkg-check-xterm.sh")
    
    if check_d3 == '0':
        xterm = 'null'
    else:
        xterm = 'inst'
    
    return xterm

def check_macchanger():
    
    check_d4 = sp.getoutput("bash etc/dpkg-check/dpkg-check-macchanger.sh")

    if check_d4 == '0':
        macchanger = 'null'
    else:
        macchanger = 'inst'

    return macchanger

def export():
    mdk3 = check_mdk3()
    aircrack = check_aircrack()
    xterm = check_xterm()
    macchanger = check_macchanger()

    if mdk3 == 'null':
        flag = "null"
    elif aircrack == 'null':
        flag = "null"
    elif xterm == 'null':
        flag = "null"
    elif macchanger == "null":
        flag = "null"
    else:
        time.sleep(1)
    
    if flag == 'null':
        os.system("echo "+flag+" > tmp/flag.txt")
    else:
        check_file()

