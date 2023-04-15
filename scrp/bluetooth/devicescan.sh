#!/bin/bash

hcitool scan | while read line
do
    mac=$(echo $line | awk '{print $1}')
    name=$(echo $line | awk '{$1=""; print $0}')
    if [[ $name == *phone* ]]
    then
        echo "Phone detected: $name [$mac]"
    fi
done
