#!/bin/bash
set -evx
PATH=/bin:/usr/bin:/sbin:/usr/sbin:/usr/games/:/usr/X11R6/bin/:/usr/bin/X11/:/games/mamelive/scripts
REP="/home/$(whoami)"
export TERM=xterm

if pidof xmamescreensaver;
then
	killall xmamescreensaver
fi

if pidof mame || pidof retroarch || pidof retroarch-zip; 
then
	exit 0
fi

RANDOM=`date '+%s'`
line0="/games/roms/mame/"
cp $REP/.mame/mame.ini /tmp
cp $REP/.xmame/cfg/saver.cfg $REP/.xmame/cfg/default.cfg

sed -i 's/$HOME\/.mame\/cfg/$HOME\/.xmame\/cfg/' /tmp/mame.ini

# la liste de fichiers où choisir
cd $line0 
ls *.zip > /tmp/tmp.txt
MAX=`ls *.zip | wc -l`
FILE=/tmp/tmp.txt
echo $MAX
# prend une ligne au hasard

number=`echo $[($RANDOM % $MAX) + 1]`
echo $number
line=`sed -n "$number"p $FILE`
# joue le jeu
/games/mamelive/scripts/xmamescreensaver -volume -15 -inipath /tmp/ $line0/$line  
$REP/configurations/livemamecab/resolution.sh &
inc=0
while [ "$inc" -lt 10 ]  
do
	if pidof mame;
	then
		killall xmamescreensaver
		killall screensaver.sh 
		exit 0
	else
		inc=`expr $inc + 1`
		sleep 3
		break
	fi 
done

# Auto restart cabrio

if pidof cabrio;
then
	exit 1
else
	cabrio
fi