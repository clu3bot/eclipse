#!/bin/bash
initial(){
int=$(cat scrp/inthandler/tmp/tmpint.csv)
sudo iwlist $int scanning | egrep 'ESSID' |  awk '!/ESSID:""/' | sed 's/^\ *//' | nl -n ln -w 6 > scrp/networkhandler/tmp/network_tmp.csv
}

run(){
initial
}

run