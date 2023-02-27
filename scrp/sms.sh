#!/bin/bash

ewr() {
    sleep 0.05
    echo -e "$@"
}

send_sms(){
   clear
   ewr "\nNOTE: SMS Messaging allows one free sms message per day, per device.\n\n"     
   ewr "Enter Number as >  1 + 234 234 6789   With No spaces"
   ewr "Example = 12342346789\n"
   ewr "Enter Phone Number With Country Code:"
   
   read -r phonenumber
   
   echo -e "\nEnter Message:"
   
   read -r sms

   smssent=$(curl -# -X POST https://textbelt.com/text --data-urlencode phone="$phonenumber" --data-urlencode message="$sms" -d key=textbelt)
   
   if grep -q true <<<"$smssent"
   
   then
      
      echo -e "\nSUCCESS"
      echo -e "----------------------------------------------"
      echo "$smssent"
      echo -e "----------------------------------------------"
   else
      echo -e "\nFAIL\n"
      echo -e "----------------------------------------------"
      echo "$smssent"
      echo -e "----------------------------------------------\n"
   fi
   echo "Press any key to return to Main Menu"
   read -r 
}

initial() {
    send_sms
}

initial