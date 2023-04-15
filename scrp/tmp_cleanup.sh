#!/bin/bash

initial() {
clear
if [ -f "scrp/inthandler/tmp/tmpint.csv" ]; then
    sudo rm -rf scrp/inthandler/tmp/tmpint.csv
else
    true
fi
if [ -f "scrp/networkhandler/tmp/network_tmp.csv" ]; then
    sudo rm -rf scrp/networkhandler/tmp/network_tmp.csv
else
    true
fi
if [ -f "scrp/networkhandler/tmp/network_finale_tmp.csv" ]; then
    sudo rm -rf scrp/networkhandler/tmp/network_finale_tmp.csv
else
    true
fi
}

run(){
    initial
}

run