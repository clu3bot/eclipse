#!/bin/bash


getvar() {
    int=$(sudo python3 scrp/inthandler/rename.py)
}

apdump() {
    sudo airmon-ng start ${int}
    sudo airodump-ng start ${int}

}

initial() {
getvar
apdump
}

initial
