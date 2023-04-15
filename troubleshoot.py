import os 
import subprocess as sp
import time
import platform

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

def clear(): #clear
    os.system('cls' if os.name == 'nt' else 'clear')

def downloads(): #checks if downloads has been run.
    check = sp.getoutput("cat etc/done_flag.csv")

    if check == 'done':
        flag_downloads = 1
    else:
        flag_downloads = 0
    
    return flag_downloads
    

def permissions():  #checks for root permissions
    if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
        flag_permissions = 0
    else:
        flag_permissions = 1

    return flag_permissions

def getos(): # checks if system is linux
    osys=platform.system()
    if osys != "Linux":
        flag_os = 0
    else:
        flag_os = 1

    return flag_os

def dependencies():
    os.system("python3 bin/ess/dependencies.py")
    check = sp.getoutput("cat bin/ess/tmp/flag.csv")

    if check == 'null':
        flag_dependencies = 0
    else:
        flag_dependencies = 1

    return flag_dependencies

def check_all():
    flag_1 = downloads()
    flag_2 = permissions()
    flag_3 = getos()
    flag_4 = dependencies()

    if flag_1 == 0:
        print (color.red+"File: install.py has not been run.")
    elif flag_2 == 0:
        print (color.red+"Program requires sudo permission.")
    elif flag_3 == 0:
        print (color.red+"Os is not Linux. This program only runs on linux")
    elif flag_4 == 0:
        print (color.red+"Missing Dependencies. Run install.py in cora/ directory.")


def display():
    clear()
    print("Diagnosing problems..\n")
    permissions()
    print("25%")
    downloads()
    print("50%")
    getos()
    print("75%")
    dependencies()
    check_all()
    print ("100%")
    clear()
    print("No problems detected.. If you are still expierencing a problem or bug please submit an Issue on the eclipse repo\n")
    input("Press anything to close..")
    exit()
display()
