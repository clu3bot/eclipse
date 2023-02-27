dpkg-query -W -f='${Status}' arp-scan 2>/dev/null | grep -c "ok installed"
