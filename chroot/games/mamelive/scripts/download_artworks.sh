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
--title="Download Artworks" \
--column="Choice" --column="Description" \
"1"        "Mame" \
"2"        "Megadrive" \
"3"        "Snes" \
"4"        "Pcengine" `

case "$opt" in

	1) f="mame" ;;

	2) f="genesis" ;;

	3) f="snes" ;;
	
	4) f="pcengine" ;;

	*) echo $opt | exit 1 ;;
esac

############################################

domain="http://mame.traceroot.fr/livemamecab"
i=0

####### Mame #######

if [ "$f" = "mame" ] 
then	

chemin="/games/artworks/mame"
cd /games/roms/mame 

zenity --info --text "Please wait check list" --timeout=2

midori http://numsys.eu/livemamecab/$f/snap &
sleep 2
midori http://numsys.eu/livemamecab/$f/marquees &
sleep 2
midori http://numsys.eu/livemamecab/$f/videos &

for i in *
do
	echo ${i%.*}
	if [ -f $chemin/snap/"${i%.*}.png" ]
	then
		zenity --info --text "${i%.*} Snap already present" --timeout=1
	else 
		cd $chemin/snap
		wget --progress=bar:force --limit-rate=64k $domain/$f/snap/"${i%.*}.png"  2>&1 | zenity --title="Snap file transfer in progress: "${i%.*}"" --progress --auto-close --auto-kill
	fi

	if [ -f $chemin/marquees/"${i%.*}.png" ]
	then
		zenity --info --text "${i%.*} Marquee already present" --timeout=1
	else 	
		cd $chemin/marquees
		wget --progress=bar:force --limit-rate=64k $domain/$f/marquees/"${i%.*}.png"  2>&1 | zenity --title="Marquee file transfer in progress : "${i%.*}"" --progress --auto-close --auto-kill
	fi	
	
	
	if [ -f $chemin/videos/"${i%.*}.flv" ] || [ -f $chemin/videos/"${i%.*}.avi" ] || [ -f $chemin/videos/"${i%.*}.mp4" ]
	then
		zenity --info --text "${i%.*} Video Already present" --timeout=1
	else 
		cd $chemin/videos
		wget --progress=bar:force --limit-rate=128k $domain/$f/videos/"${i%.*}.flv"  2>&1 | zenity --title="Video file transfer in progress : "${i%.*}"" --progress --auto-close --auto-kill
		wget --progress=bar:force --limit-rate=128k $domain/$f/videos/"${i%.*}.mp4"  2>&1 | zenity --title="Video file transfer in progress : "${i%.*}"" --progress --auto-close --auto-kill
		wget --progress=bar:force --limit-rate=128k $domain/$f/videos/"${i%.*}.avi"  2>&1 | zenity --title="Video file transfer in progress : "${i%.*}"" --progress --auto-close --auto-kill
	fi
done
thunar $chemin/snap &
fi

####### Megadrive #######


if [ "$f" = "genesis" ] 
then	

cd /games/roms/genesis 
chemin="/games/artworks/genesis"

zenity --info --text "Please wait check list" --timeout=2

midori http://numsys.eu/livemamecab/$f/snap &
sleep 2
midori http://numsys.eu/livemamecab/$f/marquees &
sleep 2
midori http://numsys.eu/livemamecab/$f/videos &

for i in *
do
	echo ${i%.*}
	if [ -f $chemin/snap/"${i%.*}.png" ]
	then
		zenity --info --text "${i%.*} Snap already present" --timeout=1
	else 
		cd $chemin/snap
		wget --progress=bar:force --limit-rate=64k $domain/$f/snap/"${i%.*}.png"  2>&1 | zenity --title="Snap file transfer in progress: "${i%.*}"" --progress --auto-close --auto-kill
	fi

	if [ -f $chemin/marquees/"${i%.*}.png" ]
	then
		zenity --info --text "${i%.*} Marquee already present" --timeout=1
	else 	
		cd $chemin/marquees
		wget --progress=bar:force --limit-rate=64k $domain/$f/marquees/"${i%.*}.png"  2>&1 | zenity --title="Marquee file transfer in progress : "${i%.*}"" --progress --auto-close --auto-kill
	fi	
	
	
	if [ -f $chemin/videos/"${i%.*}.flv" ] || [ -f $chemin/videos/"${i%.*}.avi" ] || [ -f $chemin/videos/"${i%.*}.mp4" ]
	then
		zenity --info --text "${i%.*} Video Already present"--timeout=1
	else 
		cd $chemin/videos
		wget --progress=bar:force --limit-rate=128k $domain/$f/videos/"${i%.*}.flv"  2>&1 | zenity --title="Video file transfer in progress : "${i%.*}"" --progress --auto-close --auto-kill
		wget --progress=bar:force --limit-rate=128k $domain/$f/videos/"${i%.*}.mp4"  2>&1 | zenity --title="Video file transfer in progress : "${i%.*}"" --progress --auto-close --auto-kill
		wget --progress=bar:force --limit-rate=128k $domain/$f/videos/"${i%.*}.avi"  2>&1 | zenity --title="Video file transfer in progress : "${i%.*}"" --progress --auto-close --auto-kill
	fi
done
thunar $chemin/snap &
fi


####### Snes #######


if [ "$f" = "snes" ] 
then	

cd /games/roms/snes
chemin="/games/artworks/snes"

zenity --info --text "Please wait check list" --timeout=2

midori http://numsys.eu/livemamecab/$f/snap &
sleep 2
midori http://numsys.eu/livemamecab/$f/marquees &
sleep 2
midori http://numsys.eu/livemamecab/$f/videos &

for i in *
do
	echo ${i%.*}
	if [ -f $chemin/snap/"${i%.*}.png" ]
	then
		zenity --info --text "${i%.*} Snap already present" --timeout=1
	else 
		cd $chemin/snap
		wget --progress=bar:force --limit-rate=64k $domain/$f/snap/"${i%.*}.png"  2>&1 | zenity --title="Snap file transfer in progress: "${i%.*}"" --progress --auto-close --auto-kill
	fi

	if [ -f $chemin/marquees/"${i%.*}.png" ]
	then
		zenity --info --text "${i%.*} Marquee already present" --timeout=1
	else 	
		cd $chemin/marquees
		wget --progress=bar:force --limit-rate=64k $domain/$f/marquees/"${i%.*}.png"  2>&1 | zenity --title="Marquee file transfer in progress : "${i%.*}"" --progress --auto-close --auto-kill
	fi	
	
	
	if [ -f $chemin/videos/"${i%.*}.flv" ] || [ -f $chemin/videos/"${i%.*}.avi" ] || [ -f $chemin/videos/"${i%.*}.mp4" ]
	then
		zenity --info --text "${i%.*} Video Already present" --timeout=1
	else 
		cd $chemin/videos
		wget --progress=bar:force --limit-rate=128k $domain/$f/videos/"${i%.*}.flv"  2>&1 | zenity --title="Video file transfer in progress : "${i%.*}"" --progress --auto-close --auto-kill
		wget --progress=bar:force --limit-rate=128k $domain/$f/videos/"${i%.*}.mp4"  2>&1 | zenity --title="Video file transfer in progress : "${i%.*}"" --progress --auto-close --auto-kill
		wget --progress=bar:force --limit-rate=128k $domain/$f/videos/"${i%.*}.avi"  2>&1 | zenity --title="Video file transfer in progress : "${i%.*}"" --progress --auto-close --auto-kill
	fi
done
thunar $chemin/snap &
fi

####### pcengine #######


if [ "$f" = "pcengine" ] 
then	

cd /games/roms/pcengine
chemin="/games/artworks/pcengine"

zenity --info --text "Please wait check list" --timeout=2

midori http://numsys.eu/livemamecab/$f/snap &
sleep 2
midori http://numsys.eu/livemamecab/$f/marquees &
sleep 2
midori http://numsys.eu/livemamecab/$f/videos &

for i in *
do
	echo ${i%.*}
	if [ -f $chemin/snap/"${i%.*}.png" ]
	then
		zenity --info --text "${i%.*} Snap already present" --timeout=1
	else 
		cd $chemin/snap
		wget --progress=bar:force --limit-rate=64k $domain/$f/snap/"${i%.*}.png"  2>&1 | zenity --title="Snap file transfer in progress: "${i%.*}"" --progress --auto-close --auto-kill
	fi

	if [ -f $chemin/marquees/"${i%.*}.png" ]
	then
		zenity --info --text "${i%.*} Marquee already present" --timeout=1
	else 	
		cd $chemin/marquees
		wget --progress=bar:force --limit-rate=64k $domain/$f/marquees/"${i%.*}.png"  2>&1 | zenity --title="Marquee file transfer in progress : "${i%.*}"" --progress --auto-close --auto-kill
	fi	
	
	
	if [ -f $chemin/videos/"${i%.*}.flv" ] || [ -f $chemin/videos/"${i%.*}.avi" ] || [ -f $chemin/videos/"${i%.*}.mp4" ]
	then
		zenity --info --text "${i%.*} Video Already present"--timeout=1
	else 
		cd $chemin/videos
		wget --progress=bar:force --limit-rate=128k $domain/$f/videos/"${i%.*}.flv"  2>&1 | zenity --title="Video file transfer in progress : "${i%.*}"" --progress --auto-close --auto-kill
		wget --progress=bar:force --limit-rate=128k $domain/$f/videos/"${i%.*}.mp4"  2>&1 | zenity --title="Video file transfer in progress : "${i%.*}"" --progress --auto-close --auto-kill
		wget --progress=bar:force --limit-rate=128k $domain/$f/videos/"${i%.*}.avi"  2>&1 | zenity --title="Video file transfer in progress : "${i%.*}"" --progress --auto-close --auto-kill
	fi
done
thunar $chemin/snap &
fi

