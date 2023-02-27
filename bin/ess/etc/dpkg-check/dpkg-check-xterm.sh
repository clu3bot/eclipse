#!/bin/bash/
dpkg-query -W -f='${Status}' xterm 2>/dev/null | grep -c "ok installed"
