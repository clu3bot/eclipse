import os 
import time
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


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

global interface 
interface = sp.getoutput("cat scrp/wifitools/tmp/int.txt")

def beaconrandomnames():
    clear()
    print ("Starting..")
    time.sleep(0.5)
    print (color.lightgreen+"[Beacon Spam Active]"+color.none)
    os.system("sudo mdk3 "+interface+" b -s 500")

def beaconnamesfile():
    clear()
    print ("File must be located in "+color.lightred+" /cora/scrp/wifitools/ess"+color.none)
    if os.path.isfile("scrp/wifitools/ess/file.txt"):
        defaultfile = sp.getoutput("scrp/wifitools/ess/file.txt")
    else:
        defaultfile = "Null"

    ask = input("File "+color.lightred+defaultfile+color.none+" is currently set as your default names file, is this the file you would like to use? (Y/N)")
    asklower = ask.lower()
    if asklower == "y":
        time.sleep(1)
    elif asklower == "n":
        clear()
        print ("File must be located in "+color.lightred+" /cora/scrp/wifitools/ess"+color.none)
        file = input ("What is the name of the file Including file extention. Example "+color.lightgreen+"file.txt"+color.none+": ")
    else:
        clear()
        print ("File must be located in "+color.lightred+" /cora/scrp/wifitools/ess"+color.none)
        file = input ("What is the name of the file Including file extention. Example "+color.lightgreen+"file.txt"+color.none+": ")

    if os.path.isfile("scrp/wifitools/ess/"+file):
        question = input ("Would you like to set this File as your Default File? (Y/N)")

        lowquestion = question.lower()
        if lowquestion == "y":
            os.system("echo "+file+" > scrp/wifitools/ess/file.txt")
        elif lowquestion == "n":
            time.sleep(1)
        else:
            print("Invalid Option..")
    else:
        clear()
        print("File could not be located in "+color.lightred+"/cora/scrp/wifitools/ess"+color.none)
        time.sleep(4)
        beaconnamesfile()

    


def beaconspam():

    print ("Beacon Flood Options:\n\n")
    print ("[1] Use Random Names")
    print ("[2] Use a Names File")
    i = input ("\n\nChoose an Option: ")

    if i == "1":
        beaconrandomnames()
    elif i == "2":
        beaconnamesfile()
    else:
        print ("Invalid Option")

beaconspam()

