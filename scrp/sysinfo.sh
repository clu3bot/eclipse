#!/usr/bin/env bash

#colors
#bold="(tput bold)"
magenta="\033[1;35m"
green="\033[1;32m"
white="\033[1;37m"
blue="\033[1;34m"
red="\033[1;31m"
black="\033[1;40;30m"
yellow="\033[1;33m"
cyan="\033[1;36m"
reset="\033[0m"
bgyellow="\033[1;43;33m"
bgwhite="\033[1;47;37m"
c0="${reset}"
c1="${magenta}"
c2="${green}"
c3="${white}"
c4="${blue}"
c5="${red}"
c6="${yellow}"
c7="${cyan}"
c8="${black}"
c9="${bgyellow}"
c10="${bgwhite}"

#getting the init
get_init() {
    os="$(uname -o)"
    if [[ "$os" = "Android" ]]; then
       echo "init.rc"
    elif [[ ! $(pidof systemd) ]]; then
        if [[ -f "/sbin/openrc" ]]; then
            echo "openrc"
        else
         echo $(cat /proc/1/comm)
        fi
    else
        echo "systemD"
    fi
}

#get total packages
net_pkg() {
    pack="$(which {xbps-install,apk,apt,pacman,nix,yum,rpm,dpkg,emerge} 2>/dev/null | grep -v "not found" | awk -F/ 'NR==1{print $NF}')"
  case "${pack}" in
      "xbps-install")
	 total=$(xbps-query -l | wc -l)
	 ;;
      "apk")
	 total=$(apk search | wc -l)
	 ;;
      "apt")
	 total=$(apt list --installed 2>/dev/null | wc -l)
	 ;;
      "pacman")
	 total=$(pacman -Q | wc -l)
	 ;;
      "nix")
	 total=$(nix-env -qa --installed "*" | wc -l)
	 ;;
      "yum")
	 total=$(yum list installed | wc -l)
	 ;;
      "rpm")
	 total=$(rpm -qa | wc -l)
	 ;;
      "emerge")
	 total=$(qlist -I | wc -l)
	 ;;
#      "dpkg")
#	 total=$(dpkg-query -l | wc -l)
#	 ;;
      "")
	 total="Unknown"
	 ;;
  esac

  echo $total
}

# check distro info for counting n.o of packages accordingly
distro_detect() {
	distro="$(source /etc/os-release && echo "${PRETTY_NAME}")"
}

storage_info() {
    storageused=$(df -h / | grep "/" | awk '{print $3}')
    storageavail=$(df -h / | grep "/" | awk '{print $2}')
}

# Get Memory usage
get_mem () {
  free --mega | sed -n -E '2s/^[^0-9]*([0-9]+) *([0-9]+).*/'"${space}"'\2 \/ \1 MB/p'
}
# fetch output
distro_detect
storage_info
echo -e "\n${c1}os${c3}    ${distro} $(uname -m)"
echo -e "${c2}kernal${c3}   $(uname -r)"
echo -e "${c7}packages${c3}  $(net_pkg)"
echo -e "${c4}shell${c3}    $(basename "${SHELL}")"
echo -e "${c6}ram${c3}   $(get_mem)"
echo -e "${c1}init${c3}  $(get_init)"
echo -e "${c7}uptime${c3}   $(uptime -p | sed 's/up//')"
echo -e "${c4}disk${c3}  $storageused / $storageavail\n"
echo -e "               \033[0m"
