#!/bin/bash

output() {
        unset $var
        clear
        echo -e "Available Wireless Interfaces:\n"
                ip -o -4 route show to default | awk '{print $5}' | nl -n ln -w 6 > scrp/inthandler/wifiifaces.txt
                cat scrp/inthandler/wifiifaces.txt
                y=$(wc -l scrp/inthandler/wifiifaces.txt | awk '{print $1}')
                echo -e "\n"
                read -r -p "Select:" x
                if [ "$x" -gt "$y" ]; then
                        clear
                        echo -e "Selection Invalid.. Select Again"
                        sleep 2
                        output
                elif [[ "$x" != ?(-)+([[:digit:]]) ]]; then
                        clear
                        echo -e "Selection Invalid.. Select Again"
                        sleep 2
                        output
                else
                        var=$(cat scrp/inthandler/wifiifaces.txt | awk 'NR=='${x}'' | awk '{print $2}')
                fi
                echo $var > scrp/inthandler/tmp/tmpint.txt
                clear
                python3 scrp/inthandler/tmp/stint.py
                rm -rf scrp/inthandler/wifiifaces.txt
}

output
