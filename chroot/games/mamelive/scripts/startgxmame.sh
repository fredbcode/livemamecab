#!/bin/bash
set -vx

PATH=/bin:/usr/bin:/sbin:/usr/sbin:/usr/games/:/usr/X11R6/bin/:/usr/bin/X11/:/usr/local/bin
REP="/home/$(whoami)"
$REP/configurations/livemamecab/resolution.sh &
xset -dpms
xset s off 
#xset -display :0 s off -dpms

uid=`whoami`
mount=$HOME/USB_DISK
usb=NULL

for DEV in /sys/block/sd*
do
if readlink $DEV | grep -q usb ;then
DEV=`basename $DEV`
	if [ -d /sys/block/${DEV}/${DEV}1 ] 
	then
		echo "Has partitions" /sys/block/$DEV/$DEV[0-9]*
		grep ${DEV}1 /etc/mtab
			if [ $? -ne 0 ]
				then
				echo "partition1 dispo" 
				usb=/dev/${DEV}1				
			fi 
	fi
	
	if [ -d /sys/block/${DEV}/${DEV}2 ] 
		then
                echo "Has partitions" /sys/block/$DEV/$DEV[0-9]*
                grep ${DEV}2 /etc/mtab
                        if [ $? -ne 0 ]
                        then
                                echo "partition2 dispo"
				usb=/dev/${DEV}2 
                        fi 
	fi
fi
done 


# verif livemamecab sur HDD
mount | grep sd | grep "on / " | grep -v vfat 
if [ $? = 0 ]
then
	zenity --info  --text="Livemamecab on HDD" --timeout=1 &
	usb=NULL
fi

ls $usb
if [ $? != 0 ]
then
	zenity --info  --text="Ok USB drive not found" --timeout=1 &
	thunar -q 
	cabrio
	exit 0
fi

(
	echo "10"
	zenity --info  --text="USB disk found" --timeout=3 &
	sleep 2
	mkdir $HOME/USB_DISK
	sudo umount $usb
	sudo mount -rw -o uid=$uid,relatime,utf8,umask=022 $usb $mount
	if [ $? -ne 0 ]
		then
		zenity --warning  --text="BAD Drive ..." --timeout=5 
		usb=NULL
		exit 0
	fi

	if test ! -d $mount/liveconf
		then
		opt=`zenity --list --width=350 --height=220 \
		--title="Livemamecab configuration on usb ?" \
		--column="Choice" --column="Caution irreversible process !" \
		"1"        "Yes"` \

		case "$opt" in

		1) f="yes" ;;
		*) echo $opt | exit 1 ;;
		esac


		if [ "$f" = "yes" ] 
		then
			echo "20"  
			zenity --info  --text="Create USB Directory" --timeout=3 &
			sleep 1
			mkdir $mount/liveconf
			echo "30"

		if test ! -d $mount/liveconf/mame
			then  		
			mkdir $mount/liveconf/mame
			cp -Rf $HOME/.mame/* $mount/liveconf/mame
				sleep 2
			echo "40"
		fi


		if test ! -d $mount/.retroarch.cfg
			then  		
			cp -Rf $HOME/.retroarch.cfg $mount/liveconf/.retroarch.cfg
			sleep 2
			echo "45"
		fi	

		if test ! -d $mount/liveconf/cabrio
			then  		
			mkdir $mount/liveconf/cabrio
			sleep 2
			zenity --info  --text="Create cabrio Directory - Please be patient ..." --timeout=10 &
			cp -Rf $HOME/.cabrio/* $mount/liveconf/cabrio
			echo "50"
		fi

		if test ! -d $mount/roms
			then  
			mkdir $mount/roms
			cp -Rf /games/roms/* $mount/roms
			echo "70"
			sleep 2
		fi
		else
			thunar -q
			zenity --info  --text="So, Please do not boot with USB thumb drive !" --timeout=5 &
		fi
	else
		echo "80"
		chmod 700 $mount/liveconf/script.sh &
		sleep 1
		$mount/liveconf/script.sh &
		zenity --info  --text="Find DATA" --timeout=2 &	
		rm -Rf $HOME/.mame
		rm -Rf $HOME/.cabrio
		sudo rm -Rf /games/roms
		ln -s $mount/liveconf/mame $HOME/.mame
		ln -s $mount/liveconf/cabrio $HOME/.cabrio
		ln -s $mount/liveconf/.retroarch.cfg $HOME/.retroarch.cfg
		sudo ln -s $mount/roms /games/roms 
		echo "100"
	fi
	
) | zenity --progress \
  --title="Livemamecab" \
  --text="Please wait Initializing..." \
  --percentage=0 --auto-close

thunar -q 
zenity --info --text="Enjoy !" --timeout=2 &
cabrio





