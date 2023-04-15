#!/bin/bash

x=$(hcitool dev | awk 'NR==2 {print $2}')
echo "Your Bluetooth Mac Adress is: " $x