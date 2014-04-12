#!/bin/bash
set -vx

###### Test rseau #########


ping -q -c 2 google.com >/dev/null 2>&1 
if [ $? -eq 0 ]; then 
	zenity --info --text="Network OK" --timeout 2
else 
	zenity --warning --text="No network ?" --timeout 2 || exit 0
fi


####################### choix ############################
opt=`zenity --list --width=350 --height=220 \
--title="Download/install kernel 15 khz" \
--column="Choice" --column="Description" \
"1"        "Download"` \

case "$opt" in

	1) f="downloadkernel" ;;
	*) echo $opt | exit 1 ;;
esac

############################################

domain="http://mame.traceroot.fr/livemamecab"
i=0

####### Mame #######

if [ "$f" = "downloadkernel" ] 
then	
cd /tmp/ 
wget --progress=bar:force --limit-rate=64k $domain/kernel15khz.deb  2>&1 | zenity --title="Kernel transfer in progress" --progress --auto-close --auto-kill
zenity --info --text="Done please wait: Installation in progress" --timeout=20 
zenity --password | sudo -S dpkg -i /tmp/*.deb
zenity --info --text="reboot" --timeout=2
zenity --password | sudo -S reboot
fi


