import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def initial():
    clear()
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    input_str = input("Enter message that you would like to encrypt/decrypt: ")
    value = input_str.upper()
    initialshift = int(input("Enter a shift value: "))
    shift = initialshift
    no_of_itr = len(value)
    output_str = ""

    for i in range(no_of_itr):
        current = value[i]
        location = alphabets.find(current)
        if location < 0:
            output_str += value[i]
        else:
            new_location = (location + shift)%26
            output_str += alphabets[new_location]

    new_output = output_str.lower()

    clear()
    print ("Output: "+new_output)
    return new_output

def ask():

    rotstr = initial()
    userchoice = input ("Save this string to a file? y/n")

    userchoicelower = userchoice.lower()
    if userchoicelower == 'y':
        os.system("echo "+rotstr+" > backupstrs/rotstr.csv")
        print ("File saved to cora/etc/crypto/backupstrs/")
    elif userchoicelower == 'n':
        time.sleep(1)
    else:
        print ("Invalid Option..")
        time.sleep(2)
        ask()

ask()

def last():
    clear()
    input ("Press any key to return to Crypto Menu..")

last()
