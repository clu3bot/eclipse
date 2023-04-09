##

import os
import subprocess as sp

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


def publicip():
    os.system("curl ipinfo.io/ip > /tmp/ip.txt")
    var = sp.getoutput("cat /tmp/ip.txt")
    os.system("rm -rf /tmp/ip.txt")
    clear()
    print("Your public IP address is:"+color.green+var+color.none)
    input("\nPress any key to return to main menu..")

publicip()