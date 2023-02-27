#!/bin/bash/
dpkg-query -W -f='${Status}' macchanger 2>/dev/null | grep -c "ok installed"
