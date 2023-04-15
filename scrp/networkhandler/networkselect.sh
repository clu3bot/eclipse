#!/bin/bash


initial() {
clear
if [ -f "scrp/networkhandler/tmp/network_finale_tmp.csv" ]; then
    sudo rm -rf scrp/networkhandler/tmp/network_finale_tmp.csv
else
    true
fi
if [ -f "scrp/networkhandler/tmp/network_tmp.csv" ]; then
    sudo rm -rf scrp/networkhandler/tmp/network_tmp.csv
else
    true
fi
sudo bash scrp/networkhandler/network.sh
x=$(cat scrp/networkhandler/tmp/network_tmp.csv | wc -l)
cat scrp/networkhandler/tmp/network_tmp.csv
}

second(){
echo -e "\n"
read -r -p "Please Select a Network:" var
if [ "$var" -gt "$x" ]; then
    echo "Please Select a Valid Option.."
    sleep 2
    initial
else
    network=$(cat scrp/networkhandler/tmp/network_tmp.csv | awk 'NR=='$var'' | sed -n '/"/!{/\n/{P;b}};s/"/\n/g;D')
    echo $network > scrp/networkhandler/tmp/network_finale_tmp.csv
    echo $network
fi

}
run(){
    initial
    second
}

run