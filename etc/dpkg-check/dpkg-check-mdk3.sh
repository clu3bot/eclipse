#!/bin/bash/
dpkg-query -W -f='${Status}' mdk3 2>/dev/null | grep -c "ok installed"
