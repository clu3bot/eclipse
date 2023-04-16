
#!/bin/bash

function lcs {
  local m=$1 n=$2
  local i j

  for ((i=0; i<=m; i++)); do
    for ((j=0; j<=n; j++)); do
      if ((i == 0 || j == 0)); then
        c[i,j]=0
      elif [[ ${string1:i-1:1} == ${string2:j-1:1} ]]; then
        c[i,j]=$((c[i-1,j-1]+1))
      else
        c[i,j]=$((c[i-1,j] > c[i,j-1] ? c[i-1,j] : c[i,j-1]))
      fi
    done
  done

  echo ${c[m,n]}
}

read -p "Enter a string: " input_str

related_strings=("mdk3" "beaconspam" "apdump" "deauth" "airmon-ng" "monitor" "managed" "macaddress" "networkselection" "ip" "system" "base64" "rot cypher" "bluetooth" "geoscan")

closest_string=""
max_lcs=0
for str in "${related_strings[@]}"; do
  string1=$input_str
  string2=$str
  lcs=$(lcs ${#string1} ${#string2})

  if ((lcs > max_lcs)); then
    closest_string=$str
    max_lcs=$lcs
  fi
done

if [ "$closest_string" ==  ]; then
