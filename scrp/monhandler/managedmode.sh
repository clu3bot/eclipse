#!/bin/bash

i=$(cat scrp/inthandler/tmp/tmpint.config)
rm -rf scrp/inthandler/tmpint.config

run () {
    sudo airmon-ng stop $i > scrp/inthandler/tmp/rename.config
    o=$(cat eclipse/scrp/inthandler/tmp/rename.config | grep "station" | awk '{print $NF}' | sed 's/.*]//' | tr -d '()')
    rm-rf scrp/inthandler/tmp/rename.config
    echo $o > scrp/inthandler/tmp/tmpint.config
}

run