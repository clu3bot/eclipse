#!/bin/bash

getvar() {
int=$(sudo python3 scrp/inthandler/rename.py)
}

#saves the output of the arp scan
arp_output () {
        sudo arp-scan -I $int -l | awk 'NR > 3' | head -n -3 > tmp/arpoutput-01.txt
}

#runs and arp scan and asks if user wants to save the output after
arp_command () {
            sudo arp-scan -I $int -l | awk 'NR > 3' | head -n -3
            echo -e "\nSave this output to a file? (Y/N)"
       
}

#runs and arp scan for router names and mac addresses
arp_scan () {
clear
arp_command &
echo -e "Scanning.." && sleep 2;
clear
echo -e "Output:"
read -r r
if [[ "$r" == ["yY"]* ]]; then
        arp_output &
	echo -e "Saving Output to file."
        sleep 0.7
        clear
        echo -e "Saving Output to file.."
        sleep 0.7
        clear
        echo -e "Saving Output to file..."
        sleep 0.7
        clear
        sleep 1
        echo -e "File has been saved as tmp/arpoutput-01.txt"
        sleep 2
        main_menu;
else
        clear
        echo -e "Returning to Main Menu.."
	sleep 1.5
        main_menu;
fi
}

initial() {
    getvar
    arp_scan
}

initial
