#!/bin/bash/
dpkg-query -W -f='${Status}' aircrack-ng 2>/dev/null | grep -c "ok installed"
