#!/bin/bash

output=$(cat scrp/inthandler/tmp/tmpint.config)
mode=$(iwconfig "$output" | sed -n '/Mode:/s/.*Mode://; s/ .*//p' | awk NR==2) 
echo $mode