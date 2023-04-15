#!/bin/bash

getvar() {
int=$(cat scrp/inthandler/tmp/tmpint.csv)
}

#saves the output of the arp scan
arp_output () {
        sudo arp-scan -I $int -l | awk 'NR > 3' | head -n -3 &> scrp/wifitools/tmp/arpoutput-01.csv
}

#runs and arp scan and asks if user wants to save the output after
arp_command () {
            sudo arp-scan -I $int -l | awk 'NR > 3' | head -n -3
       
}

#runs and arp scan for router names and mac addresses
arp_scan () {
clear
arp_command &
echo -e "Scanning..\n" && sleep 2;
echo -e "\nOutput:"
echo -e "\nSave this output to a file? (Y/N)"
read -r r
if [[ "$r" == ["yY"]* ]]; then
        arp_output
        clear
	echo -e "Saving Output to file."
        sleep 1
        echo -e "File has been saved as scrp/wifitools/tmp/arpoutput-01.csv"
        sleep 2
else
        clear
        echo -e "Returning to Main Menu.."
	sleep 1.5
fi
}

initial() {
    getvar
    arp_scan
}

initial
