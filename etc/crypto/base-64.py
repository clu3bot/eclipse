import base64
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def last():
    clear()
    input ("Press any key to return to Crypto Menu..")

def ask():

    clear()
    print (base64str)
    userchoice = input ("Save this string to a file? y/n")

    userchoicelower = userchoice.lower()
    if userchoicelower == 'y':
        os.system("echo "+base64str+" > backupstrs/base64str.txt")
        print ("File saved to cora/etc/crypto/backupstrs/")
    elif userchoicelower == 'n':
        time.sleep(1)
    else:
        print ("Invalid Option..")
        time.sleep(2)
        ask()

def encode():

    clear()

    userinput = input("Encode base64: ")
    inputencode = userinput.encode("ascii")
  
    base64encode = base64.b64encode(inputencode)
    global base64str
    base64str = base64encode.decode("ascii")
  
    print("Encoded string: "+base64str)

    ask()

def decode():
    clear()
    userinput = input("Decode base64: ")
    inputdecode = base64.b64decode(userinput)

    global base64str
    base64str = str(inputdecode)
    print("Decoded string: "+base64str)

    ask()

def menu():
    clear()

    print ("1. Encode")
    print ("2. Decode")

    usernumber = input("\nSelect an Option: ")

    if usernumber == "1":
        encode()
    elif usernumber == "2":
        decode()
    else:
        time.sleep(1)
        print ("Invalid option")

menu()

def last():
    clear()
    input ("Press any key to return to Crypto Menu..")
