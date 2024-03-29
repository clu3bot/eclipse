#!/bin/bash

LBLUE='\033[1;34m'
LRED='\033[1;31m'
LGREEN='\033[1;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NONE='\033[0m'
FN="ESP8266_Deauther_v2.0.0_1MB.bin"
#

# Fix everything redo it all its absolute dog shit code L
clear
read -p "Press Enter to Clone Necessary Packages (Esptool).."
echo -e "${LRED}Downloading Esptool${NONE}"
cd Files
git clone https://github.com/espressif/esptool.git
echo -e "${LRED}Esptool Cloned Successfully${NONE}"
cd -
#
clear
        echo -e "${LBLUE}Step 1 Find ttyUSB port number${NONE}"
read -p "Press Enter to Scan for ttyUSB port number"
dmesg | grep --color=always -e "ttyUSB"
        echo -e "${RED}(See number attached to highlighted ttyUSB)${NONE}"
read -p "What is the Port Number: " PN

clear

PS3='Choose an Option -- ' 
while true; do
        echo -e "${LBLUE}Step 2 Time to Flash${NONE}"
options=("Flash Device with ($FN) on (USB PORT $PN)" "Rescan ttyUSB port number" "Choose File (Currently $FN)" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Flash Device with ($FN) on (USB PORT $PN)")
            echo "Flashing Device"
clear
cd Files
esptool.py -p /dev/ttyUSB$PN write_flash -fm qio 0x0 $FN
        echo -e "${LRED}Flashing done${NONE}"
        echo -e "${RED}(If you get no such file or directory error rescan and choose the correct port number Otherwise disregard this message)${NONE}"
break
            ;;
        "Scan ttyUSB Port")
dmesg | grep --color=always -e "ttyUSB"
echo -e "${RED}(See number attached to highlighted ttyUSB)${NONE}"
read -p "What is the Port Number: " PN
break
;;
        "Rescan ttyUSB port number")
        clear
        echo -e "${LBLUE}Rescan for ttyUSB port number${NONE}"
read -p "Press Enter to Scan for ttyUSB port number"
dmesg | grep --color=always -e "ttyUSB"
        echo -e "${RED}(See number attached to highlighted ttyUSB)${NONE}"
read -p "What is the Port Number: " PN
clear
break
;;

        "Choose File (Currently $FN)")
        clear
        echo -e "${LBLUE} Choose file (type full file name)${NONE}"
read -p "What is the name of the file: " FN

break
;;

        "Quit")
            exit
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
done