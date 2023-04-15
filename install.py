import subprocess as sp
import os
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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def permissions():  #checks for root permissions
    clear()
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

#dependencies
class dependencies:
    dependency1 = 'mdk3'
    dependency2 = 'aircrack-ng'
    dependency3 = 'xterm'
    dependency4 = 'macchanger'
    dependency5 = 'arp-scan'

#general
prompt1 = 'Install Missing Dependencies? y/n\n'
prompt2 = 'All Dependencies installed.'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_mdk3():
    
    check_d1 = sp.getoutput("bash etc/dpkg-check/dpkg-check-mdk3.sh")

    if check_d1 == '0': 
        mdk3 = 'null'
    else:
        mdk3 = 'installed'

    return mdk3

def check_aircrack():
    
    check_d2 = sp.getoutput("bash etc/dpkg-check/dpkg-check-aircrack-ng.sh")    
    
    if check_d2 == '0':
        aircrack = 'null'
    else:
        aircrack = 'installed'
    
    return aircrack

def check_xterm():
    check_d3 = sp.getoutput("bash etc/dpkg-check/dpkg-check-xterm.sh")
    
    if check_d3 == '0':
        xterm = 'null'
    else:
        xterm = 'installed'
    
    return xterm

def check_macchanger():
    
    check_d4 = sp.getoutput("bash etc/dpkg-check/dpkg-check-macchanger.sh")

    if check_d4 == '0':
        macchanger = 'null'
    else:
        macchanger = 'installed'

    return macchanger

def check_arpscan():
    
    check_d5 = sp.getoutput("bash etc/dpkg-check/dpkg-check-arpscan.sh")

    if check_d5 == '0':
        arpscan = 'null'
    else:
        arpscan = 'installed'

    return arpscan

def check_all():

    mdk3 = check_mdk3()
    aircrack = check_aircrack()
    xterm = check_xterm()
    macchanger = check_macchanger()
    arpscan = check_arpscan()

    #display

    clear()

    if mdk3 == 'null':
        print (color.red+dependencies.dependency1+" (Not Installed)"+color.none)
    else:
        print (color.green+dependencies.dependency1+" (Intsalled)"+color.none)

    if aircrack == 'null':
        print (color.red+dependencies.dependency2+" (Not Installed)"+color.none)
    else:
        print (color.green+dependencies.dependency2+" (Intsalled)"+color.none)

    if xterm == 'null':
        print (color.red+dependencies.dependency3+" (Not Intsalled)"+color.none)
    else:
        print (color.green+dependencies.dependency3+" (Intsalled)"+color.none)
    
    if macchanger == 'null':
        print (color.red+dependencies.dependency4+" (Not Intsalled)"+color.none)
    else:
        print (color.green+dependencies.dependency4+" (Intsalled)"+color.none)

    if arpscan == 'null':
        print (color.red+dependencies.dependency5+" (Not Intsalled)"+color.none)
    else:
        print (color.green+dependencies.dependency5+" (Intsalled)"+color.none)

def download():

    mdk3 = check_mdk3()
    aircrack = check_aircrack()
    xterm = check_xterm()
    macchanger = check_macchanger()
    arpscan = check_arpscan()

    download_check_apt = sp.getoutput("command -v apt-get")
    download_check_apk = sp.getoutput("command -v apk")
    download_check_dnf = sp.getoutput("command -v dnf")
    download_check_zypper = sp.getoutput("command -v zypper")
    download_check_pacman = sp.getoutput("command -v pacman")

    if download_check_apt != ' ':
        packman = 'apt'
    elif download_check_apk != ' ':
        packman = 'apk'
    elif download_check_dnf != ' ':
        packman = 'dnf'
    elif download_check_zypper != ' ':
        packman = 'zypper'
    elif download_check_pacman != ' ':
        packman = 'pacman'
    else:
        print ("Could not locate a package manager.")
        exit()
    
    if mdk3 == 'null':
        if packman == 'apt':
            os.system("sudo apt-get install mdk3")
        elif packman == 'apk':
            os.system("sudo apk add mdk3")
        elif packman == 'dnf':
            os.system("sudo dnf install mdk3")
        elif packman == 'zypper':
            os.system("sudo zypper install mdk3")
        elif packman == 'pacman':
            os.system("sudo pacman -S mdk3")
        else:
            print("Could not locate a package..")
    elif aircrack == 'null':
        if packman == 'apt':
            os.system("sudo apt-get install aircrack-ng")
        elif packman == 'apk':
            os.system("sudo apk add aircrack-ng")
        elif packman == 'dnf':
            os.system("sudo dnf install aircrack-ng")
        elif packman == 'zypper':
            os.system("sudo zypper install aircrack-ng")
        elif packman == 'pacman':
            os.system("sudo pacman -S aircrack-ng")
        else:
            print("Could not locate a package..")
    elif xterm == 'null':
        if packman == 'apt':
            os.system("sudo apt-get install xterm")
        elif packman == 'apk':
            os.system("sudo apk add xterm")
        elif packman == 'dnf':
            os.system("sudo dnf install xterm")
        elif packman == 'zypper':
            os.system("sudo zypper install xterm")
        elif packman == 'pacman':
            os.system("sudo pacman -S xterm")
        else:
            print("Could not locate a package..")
    elif macchanger == 'null':
        if packman == 'apt':
            os.system("sudo apt-get install macchanger")
        elif packman == 'apk':
            os.system("sudo apk add macchanger")
        elif packman == 'dnf':
            os.system("sudo dnf install macchanger")
        elif packman == 'zypper':
            os.system("sudo zypper install macchanger")
        elif packman == 'pacman':
            os.system("sudo pacman -S macchanger")
        else:
            print("Could not locate a package..")
    elif arpscan == 'null':
        if packman == 'apt':
            os.system("sudo apt-get install arp-scan")
        elif packman == 'apk':
            os.system("sudo apk add arp-scan")
        elif packman == 'dnf':
            os.system("sudo dnf install arp-scan")
        elif packman == 'zypper':
            os.system("sudo zypper install arp-scan")
        elif packman == 'pacman':
            os.system("sudo pacman -S arp-scan")
        else:
            print("Could not locate a package..")
    else:
        print ("Could not locate a package.")
    

def ask():
    a = input(prompt1)
    b = a.lower()
    if b == 'y':
        download()
    elif b == 'n':
        print (color.red+"Warning Cora will loose function if these packages are not installed."+color.none)
        input ("Press any key to continue..")
        time.sleep(3)
    else:
        print (color.red+"Invalid Option"+color.none)

def prompt():

    mdk3 = check_mdk3()
    aircrack = check_aircrack()
    xterm = check_xterm()
    macchanger = check_macchanger()
    arpscan = check_arpscan()

    if mdk3 == 'null':
        check = 0
    elif aircrack == 'null':
        check = 0
    elif xterm == 'null':
        check = 0
    elif macchanger == 'null':
        check = 0
    elif arpscan == 'null':
        check = 0
    else:
        check = 1

    if check == 0:
        ask()
    elif check == 1:
        print (prompt2)
    else:
        print (color.red+"Error"+color.none)

def export_done_flag():
    done_flag = 'done'
    os.system("echo "+done_flag+" > bin/config/eclipse_config_done_flag.config")

def initialload():
    check_mdk3()
    check_aircrack()
    check_xterm()
    check_macchanger()
    check_arpscan()
    check_all()
    prompt()
    export_done_flag()

initialload()
