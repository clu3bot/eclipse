#!/bin/bash
red="\033[1;31m"
reset="\033[0m"

rm -rf scrp/inthandler/tmp/tmpint.config

output() {
        unset $var
        clear
        echo -e "Available Wireless Interfaces:\n"
                
                echo -e "[s] Skip"
                echo -e "[x] Exit\n"
                ip -o -4 route show to default | awk '{print $5}' | nl -n ln -w 6 > scrp/inthandler/wifiifaces.csv
                cat scrp/inthandler/wifiifaces.csv
                y=$(wc -l scrp/inthandler/wifiifaces.csv | awk '{print $1}')
                echo -e "\n"
                echo -e "If you have do not see any interfaces, skip and run the interface_troubleshoot command in the Eclipse Dev Terminal"
                read -r -p "Select:" x
                if [ "$x" = "x" ]; then
                        clear
                        exit
                elif [ "$x" = "s" ]; then
                        rm -rf scrp/inthandler/tmp/tmpint.config
                        var="Not Selected"
                elif [ "$x" -gt "$y" ]; then
                        clear
                        echo -e $red"Selection Invalid.. Select Again"$reset
                        sleep 2
                        output
                elif [[ "$x" != ?(-)+([[:digit:]]) ]]; then
                        clear
                        echo -e $red"Selection Invalid.. Select Again"$reset
                        sleep 2
                        output
                else
                        var=$(cat scrp/inthandler/wifiifaces.csv | awk 'NR=='${x}'' | awk '{print $2}')
                fi
                echo $var > scrp/inthandler/tmp/tmpint.config
                clear
                python3 scrp/inthandler/tmp/stint.py
                rm -rf scrp/inthandler/wifiifaces.csv
}

monitortest
output
