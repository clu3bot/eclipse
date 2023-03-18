import sys
import random as rd
import os
import time
import threading as thd
import subprocess as sp
import signal
import os.path
import platform
import argparse as ag
import socket as so

#name vars
class nvar:
    version="1.0 Beta"
    user="clu3bot"
    date="2023"
    project="Eclipse"

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

#clears terminal when called
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#captures ctrl c
def handleexit():
    def signal_handler(signal, frame):
        clear()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

#convert to standalone
#checks for super user perms
def permissions():
    clear()
    if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
        print(color.lightred + "You need to run this script with sudo or as root.")
        time.sleep(0.3)
        quit()
        
#convert to standalone
#varifies os is Linux or quits
def getos():
    osys=platform.system()
    if osys != "Linux":
        print(color.lightred + "This program only runs on Linux operating systems.")
        time.sleep(2)
        quit()

#convert to standalone
#checks for dns connection by pinging google
def internet_on(host="8.8.8.8", port=53, timeout=3):

    try:
        so.setdefaulttimeout(timeout)
        so.socket(so.AF_INET, so.SOCK_STREAM).connect((host, port))
        return True
    except so.error as ex:
        print(ex)
        return False

#prompts user when a part of the script requires internet
def nointernetprompt():
    clear()
    print (color.lightred+"This Option Requires Internet.."+color.none)
    time.sleep(2)

#runs the iptracing script
def iptrace():
    if internet_on() is True:
        os.system("sudo perl scrp/iptrace.pl")
    else:
        nointernetprompt()

#checks if the flag created by install.py exists to varify install requirements have been checked.
def check_install():
    check = sp.getoutput("cat etc/done_flag.txt")
    if check == 'done':
        time.sleep(1)
    else:
        print(color.red+"Run install.py")
        exit()

#runs the update script
def update():
    os.system("sudo bash updates.sh")

#prompts user to check for updates
def updateprompt():
    clear()
    print ("Would you like to check for updates? (y/n)")
    updatechoice = input(":")
    if updatechoice.lower() == "y":
        update()
    elif updatechoice.lower() == "n":
        time.sleep(0.1)
    else:
        clear()
        print (color.lightred+"Invalid Selection.."+color.none)
        time.sleep(2)
        updateprompt()

#rewrite
def monitorprompt():
    clear()

#gets the wireless interface name and puts it to a variable
def getinterface():
    from scrp.inthandler.tmp.stint import var
    global interfacecurrent
    interfacecurrent = var

#runs the selectint script
def selectint():
    os.system("sudo bash scrp/inthandler/selectint.sh")
    getinterface()

def check_essid():
    if os.path.exists("scrp/tmp/essid.txt"):
        essid = sp.getoutput("cat scrp/tmp/essid.txt")
        return essid
    else:
        essid = "N/A"
        return essid

def monitoron():
    os.system("sudo bash scrp/monhandler/monitormode.sh")
    main_menu()

def monitoroff():
    os.system("sudo bash scrp/monhandler/managedmode.sh")

def selectintmainmenu():
    os.system("sudo bash scrp/inthandler/selectint.sh")
    getinterface()
    main_menu()

def selectnet():
    clear()
    os.system("sudo bash scrp/networkselect.sh")
    time.sleep(2)
    main_menu()

#convert to standalone
def publicip():   #fix to check internet/dns
    os.system("curl ipinfo.io/ip > /tmp/ip.txt")
    var = sp.getoutput("cat /tmp/ip.txt")
    os.system("rm -rf /tmp/ip.txt")
    clear()
    print("Your public IP address is:"+color.green+var+color.none)
    input("\nPress any key to return to main menu..")
    main_menu()

#function to call system info script
def sysinfo():
    clear()
    os.system("sudo bash scrp/sysinfo.sh")
    input ("Press any key to return to Main Menu..")
    main_menu()

def devmisc(): #fix

    time.sleep(1)

def sms():
    clear()

    os.system("sudo bash scrp/sms.sh")

###

#menu for spoof mac
spoofmenu_actions  = {}  

def spoof_menu():

    handleexit()
    var = sp.getoutput("cat tmp/var.txt")
    clear()
    print ("Mac Adress Options")
    print ("By "+nvar.user+", "+nvar.date)
    print ("Detailed documentation on the cora wiki found on https://github.com/clu3bot/cora\n\n")   ##fix 
    print ("[0] Set Mac Address to a random Mac\n")
    print ("[1] Choose your own Mac address"+"               [2] Reset Mac address to original\n")
    print ("[b] back")
    print ("[x] exit")
    print ("\n")
    choice = input("\n>>  ")
    spoofexec_menu(choice)

    return

#decides which option to call
def spoofexec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        spoofmenu_actions['main_menu']()
    else:
        try:
            spoofmenu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            spoofmenu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu
def spoofmacoption0():
    print ("random mac")
    time.sleep(2)
    main_menu()

def spoofmacoption1():
    print ("choose mac")
    time.sleep(2)    
    wifi_menu()

def spoofmacoption2():
    print ("reset to original mac")
    time.sleep(2)    
    bluetooth_menu()

spoofmenu_actions = {
    'main_menu': spoof_menu,
    '0': spoofmacoption0,
    '1': spoofmacoption1,    
    '2': spoofmacoption2,
    'b': back,
    'x': exit,
}

###

misc_menu_actions  = {}  

def misc_menu():

    handleexit()
    var = sp.getoutput("cat temp/var.txt")
    clear()
    print ("Misc Tool Options")
    print ("By "+nvar.user+", "+nvar.date)
    print ("Detailed documentation on the cora wiki found on https://github.com/clu3bot/\n\n")   ##fix 
    print ("[0] Search for a tool.\n")
    print ("[1] Dev Terminal"
    )
    print ("[2] Send Sms")  
    print ("[3] IP Trace / Geo Trace")
    print ("[4] Payload Tools")
    print ("[5] Hardware Tools") 
    print ("[6] Cryptography Tools"+"       [b] back")
    print ("[7] Misc Tools"+"               [x] exit")
    print ("\n")
    choice = input("\n>>  ")
    misc_exec_menu(choice)

    return

#decides which option to call
def misc_exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        misc_menu_actions['main_menu']()
    else:
        try:
            misc_menu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            misc_menu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    misc_menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu
def miscoption0():
    print ("option 0")
    time.sleep(2)
    misc_menu()

def miscoption1():
    devmisc()

def miscoption2():
    sms()

def miscoption3():
    iptrace()

def miscoption4():
    print ("option 4")
    time.sleep(2)
    misc_menu()

def miscoption5():
    print ("option 5")
    time.sleep(2)    
    misc_menu()

def miscoption6():
    print ("option 6")
    time.sleep(2)    
    misc_menu()

def miscoption7():
    print ("option 7")
    time.sleep(2)
    misc_menu()

def miscoption8():
    print ("option 8")
    time.sleep(2)
    misc_menu()

def miscoption9():
    print ("option 9")
    time.sleep(2)
    misc_menu()

def miscoption10():
    print ("option 10")
    time.sleep(2)
    misc_menu()

def miscoption11():
    print ("option 11")
    time.sleep(2)
    misc_menu()

def miscoption12():
    print ("option 12")
    time.sleep(2)
    misc_menu()

def miscoption13():
    print ("option 13")
    time.sleep(2)
    misc_menu()

#binds the options to numbers
misc_menu_actions = {
    'main_menu': misc_menu,
    '0': miscoption0,
    '1': miscoption1,    
    '2': miscoption2,
    '3': miscoption3,
    '4': miscoption4,
    '5': miscoption5,
    '6': miscoption6,
    '7': miscoption7,
    '8': miscoption8, 
    '9': miscoption9,
    '10': miscoption10,
    '11': miscoption11, 
    '12': miscoption12,
    '13': miscoption13,
    'b': back,
    'x': exit,
}

###

crypto_menu_actions  = {}  

def crypto_menu():

    handleexit()
    var = sp.getoutput("cat temp/var.txt")
    clear()
    print ("Cryptography Tool Options")
    print ("By "+nvar.user+", "+nvar.date)
    print ("Detailed documentation on the cora wiki found on https://github.com/clu3bot/cora\n\n")   ##fix 
    print ("[1] Base64 Encode/Decode"+"               [8] ")
    print ("[2] Rot Cypher Encode/Decode"+"          [9] ")  
    print ("[b] back")
    print ("[x] exit")
    print ("\n")
    choice = input("\n>>  ")
    crypto_exec_menu(choice)

    return

#decides which option to call
def crypto_exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        crypto_menu_actions['main_menu']()
    else:
        try:
            crypto_menu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            crypto_menu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu

def cryptooption1():
    os.system("python3 etc/crypto/base-64.py")
    crypto_menu()

def cryptooption2():
    os.system("python3 etc/crypto/rot-cypher.py")
    crypto_menu()

def cryptooption3():
    print ("option 3")
    time.sleep(2)
    crypto_menu()

def cryptooption4():
    print ("option 4")
    time.sleep(2)
    crypto_menu()

def cryptooption5():
    print ("option 5")
    time.sleep(2)    
    crypto_menu()

def cryptooption6():
    print ("option 6")
    time.sleep(2)    
    crypto_menu()

def cryptooption7():
    print ("option 7")
    time.sleep(2)
    crypto_menu()

def cryptooption8():
    print ("option 8")
    time.sleep(2)
    crypto_menu()

def cryptooption9():
    print ("option 9")
    time.sleep(2)
    crypto_menu()

def cryptooption10():
    print ("option 10")
    time.sleep(2)
    crypto_menu()

def cryptooption11():
    print ("option 11")
    time.sleep(2)
    crypto_menu()

def cryptooption12():
    print ("option 12")
    time.sleep(2)
    crypto_menu()

def cryptooption13():
    print ("option 13")
    time.sleep(2)
    crypto_menu()

#binds the options to numbers
crypto_menu_actions = {
    'main_menu': crypto_menu,
    '1': cryptooption1,    
    '2': cryptooption2,
    '3': cryptooption3,
    '4': cryptooption4,
    '5': cryptooption5,
    '6': cryptooption6,
    '7': cryptooption7,
    '8': cryptooption8, 
    '9': cryptooption9,
    '10': cryptooption10,
    '11': cryptooption11, 
    '12': cryptooption12,
    '13': cryptooption13,
    'b': back,
    'x': exit,
}

###

hardware_menu_actions = {}

def hardware_menu():

    handleexit()
    var = sp.getoutput("cat temp/var.txt")
    clear()
    print ("Hardware Tool Options")
    print ("By "+nvar.user+", "+nvar.date)
    print ("Detailed documentation on the cora wiki found on https://github.com/clu3bot/cora\n\n")   ##fix 
    print ("[1] Flash Bin Files to Development Boards")
    print ("[2] Burn ISO File to Live USB")  
    print ("[3] View Hardware Info\n")
    print ("[b] back")
    print ("[x] exit")
    print ("\n")
    choice = input("\n>>  ")
    hardware_exec_menu(choice)

    return

#decides which option to call
def hardware_exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        hardware_menu_actions['main_menu']()
    else:
        try:
            hardware_menu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            hardware_menu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu
def hardwareoption0():
    print ("option 0")
    time.sleep(2)
    hardware_menu()

def hardwareoption1():
    print ("wifi option 1")
    time.sleep(2)    
    hardware_menu()

def hardwareoption2():
    print ("option 2")
    time.sleep(2)    
    hardware_menu()

def hardwareoption3():
    print ("option 3")
    time.sleep(2)
    hardware_menu()

#binds the options to numbers
hardware_menu_actions = {
    'main_menu': hardware_menu,
    '0': hardwareoption0,
    '1': hardwareoption1,    
    '2': hardwareoption2,
    '3': hardwareoption3,
    'b': back,
    'x': exit,
}

###

scan_menu_actions  = {}  

def scan_menu():

    handleexit()
    var = sp.getoutput("cat temp/var.txt")
    clear()
    print ("Prefabricated Scan Options")
    print ("By "+nvar.user+", "+nvar.date)
    print ("Detailed documentation on the cora wiki found on https://github.com/clu3bot/cora\n\n")   ##fix 
    print ("[1] ARP Scan")
    print ("[2] NMAP Scan")  
    print ("[3] Verbose NMAP Scan")
    print ("[4] Bluetooth AP Scan")
    print ("[5] Wireless AP Dump")
    print ("[6] Gobuster Scan")
    print ("                           [b] back")
    print ("                           [x] exit")
    print ("\n")
    choice = input("\n>>  ")
    scan_exec_menu(choice)

    return

#decides which option to call
def scan_exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        scan_menu_actions['main_menu']()
    else:
        try:
            scan_menu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            scan_menu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu
def scanoption0():
    print ("option 0")
    time.sleep(2)
    scan_menu()

def scanoption1():
    print ("wifi option 1")
    time.sleep(2)    
    scan_menu()

def scanoption2():
    print ("option 2")
    time.sleep(2)    
    scan_menu()

def scanoption3():
    print ("option 3")
    time.sleep(2)
    scan_menu()

def scanoption4():
    print ("option 4")
    time.sleep(2)
    scan_menu()

def scanoption5():
    print ("option 5")
    time.sleep(2)    
    scan_menu()

def scanoption6():
    print ("option 6")
    time.sleep(2)    
    scan_menu()


#binds the options to numbers
scan_menu_actions = {
    'main_menu': scan_menu,
    '0': scanoption0,
    '1': scanoption1,    
    '2': scanoption2,
    '3': scanoption3,
    '4': scanoption4,
    '5': scanoption5,
    '6': scanoption6,
    'b': back,
    'x': exit,
}

###


bluetooth_menu_actions  = {}  

def bluetooth_menu():

    handleexit()
    var = sp.getoutput("cat temp/var.txt")
    clear()
    print ("Bluetooth Tool Options")
    print ("By "+nvar.user+", "+nvar.date)
    print ("Detailed documentation on the cora wiki found on https://github.com/clu3bot/cora\n\n")   ##fix 
    print ("[1] Bluetooth Dos"+"               [3] View Bluetooth Mac")
    print ("[2] Spoof Bluetooth Mac")  
    print ("[b] back")
    print ("[x] exit")
    print ("\n")
    choice = input("\n>>  ")
    wifi_exec_menu(choice)

    return

#decides which option to call
def bluetooth_exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        bluetooth_menu_actions['main_menu']()
    else:
        try:
            bluetooth_menu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            bluetooth_menu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    bluetooth_menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu

def btoption1():
    print ("wifi option 1")
    time.sleep(2)    
    bluetooth_menu()

def btoption2():
    print ("option 2")
    time.sleep(2)    
    bluetooth_menu()

def btoption3():
    print ("option 3")
    time.sleep(2)
    bluetooth_menu()


#binds the options to numbers
bluetooth_menu_actions = {
    'main_menu': bluetooth_menu,
    '1': btoption1,    
    '2': btoption2,
    '3': btoption3,
    'b': back,
    'x': exit,
}

###wifi

def beaconspam():
    monitorprompt()
    os.system("sudo python3 scrp/wifitools/beacon.py")

def arpscan():
    os.system("sudo bash scrp/wifitools/arpscan.sh")

def authdos():
    pass

###

def beaconspamcall():
    beaconspam()

def authdoscall():
    authdos()

def rougeapcall():
    os.system("sudo bash scrp/wifitools/rougeap.sh")

def deauthcall():
    os.system("sudo bash scrp/wifitools/deauth.sh")

def tkipcall():
    os.system("sudo bash scrp/wifitools/tkip.sh")

def apdumpcall():
    os.system("sudo bash scrp/wifitools/apdump.sh")

def arpscancall():
    arpscan()

###
wifi_menu_actions  = {}  

def wifi_menu():

    handleexit()
    var = sp.getoutput("cat temp/var.txt")
    clear()
    print ("Wifi Tool Options")
    print ("By "+nvar.user+", "+nvar.date)
    print ("Detailed documentation on the cora wiki found on https://github.com/clu3bot/cora\n\n")   ##fix 
    print ("[1] Beacon/AP Spam")
    print ("[2] Auth Dos Attack")  
    print ("[3] Rouge AP")
    print ("[4] Deauth Airplay Attack")
    print ("[5] TKIP Attack")
    print ("[6] AP Dump (See All nearby APs and Macs)"+"            ["+color.lightred+"b"+color.none+"] back")
    print ("[7] ARP Scan"+"                                         ["+color.lightred+"x"+color.none+"] exit")
    print ("\n")
    choice = input("\n>>  ")
    wifi_exec_menu(choice)

    return

#decides which option to call
def wifi_exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        wifi_menu_actions['main_menu']()
    else:
        try:
            wifi_menu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            wifi_menu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu

def wifioption1():
    beaconspamcall()

def wifioption2():
    authdoscall()

def wifioption3():
    rougeapcall()

def wifioption4():
    deauthcall()

def wifioption5():
    tkipcall()

def wifioption6():
    apdumpcall()

def wifioption7():
    arpscancall()


#binds the options to numbers
wifi_menu_actions = {
    'main_menu': wifi_menu,
    '1': wifioption1,    
    '2': wifioption2,
    '3': wifioption3,
    '4': wifioption4,
    '5': wifioption5,
    '6': wifioption6,
    '7': wifioption7,
    'b': back,
    'x': exit,
}

def animation():
    clear()

#defines the main menu
menu_actions  = {}  

def main_menu():
    getinterface()
    handleexit()
    clear()
    essid = check_essid()
    #astatus = sp.getoutput("cat scrp/etc/animationstatus.txt")
    #if astatus == "0":
    #    animation()
    #elif astatus == "1":
    #    pass
    #else:
    #    print(color.lightred+"Error")
    clear()    
    print ("By "+nvar.user+", "+nvar.date+ "       Version: "+color.green+ nvar.version+color.none+"     Interface: "+color.green+interfacecurrent+color.none+    "    Network: "+color.green+essid+color.none)
    print ("Detailed documentation on the eclipse wiki found on https://github.com/clu3bot/eclipse\n\n") 
    print ("[0] Search for a tool.\n")
    print ("[1] WiFi Tools"+"               [7] Spoof Mac Adress")
    print ("[2] Bluetooth Tools"+"          [8] Enable Monitor Mode")  
    print ("[3] Prefabricated Scans"+"      [9] Disable Monitor Mode")
    print ("                             [10] Select a Wireless Interface")
    print ("                             [11] Select a Target Network")
    print ("[4] Hardware Tools"+"           [12] Show Public IP")
    print ("[5] Cryptography Tools"+"       [13] Show System Info")
    print ("[6] Misc Tools"+"               ["+color.lightred+"x"+color.none+"] exit")
    print ("                             ["+color.lightred+"u"+color.none+"] check for updates")
    print ("\n")
    choice = input("\n>>  ")
    exec_menu(choice)

    return

#decides which option to call
def exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print (color.lightred + "Invalid selection, please try again.\n" + color.lightblue)
            time.sleep(1)
            menu_actions['main_menu']()
    return

#back to the main menu when called
def back():
    menu_actions['main_menu']()

#exits program when called
def exit():
    sys.exit()

#defines the options for the main menu
def option0():
    time.sleep(2)
#    searchvar()

def option1():
    time.sleep(2)    
    wifi_menu()

def option2():
    time.sleep(2)    
    bluetooth_menu()

def option3():
    time.sleep(2)
    scan_menu()

def option5():
    time.sleep(2)    
    hardware_menu()

def option6():
    time.sleep(2)    
    crypto_menu()

def option7():
    time.sleep(2)
    misc_menu()

def option8():
    time.sleep(2)
    spoof_menu()

def option9():
    time.sleep(2)
    monitoron()

def option10():
    time.sleep(2)
    monitoroff()

def option11():
    time.sleep(2)
    selectintmainmenu()

def option12():
    time.sleep(2)
    selectnet()

def option13():
    time.sleep(2)
    publicip()

def option14():
    time.sleep(2)
    sysinfo()

def update():
    os.system("sudo bash updates.sh")
#binds the options to numbers
menu_actions = {
    'main_menu': main_menu,
    '0': option0,
    '1': option1,    
    '2': option2,
    '3': option3,
    '4': option5,
    '5': option6,
    '6': option7,
    '7': option8, 
    '8': option9,
    '9': option10,
    '10': option11, 
    '11': option12,
    '12': option13,
    '13': option14,
    'b': back,
    'x': exit,
    'u': update,
}

#what is done on script startup
def onstartup():
    clear()
    permissions()
    check_install()
    updateprompt()
    monitorprompt()
    selectint()
    if interfacecurrent is None:
        selectint()
    else:
        time.sleep(0.5)
    if os.path.isfile("install.sh"):
        print ("please run the install.sh file in the "+nvar.project+"/ directory")
    else:
        time.sleep(0.5)
        main_menu()
onstartup()
