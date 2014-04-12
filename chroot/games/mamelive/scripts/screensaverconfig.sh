#!/bin/bash

set -vx
crontab -l > /tmp/cron

START=$(zenity --list --radiolist --height=300 --width=450 \
    --title="Livemamecab screensaver : Options" \
    --text="Randomly playing games at intervals you specify,\nthis tool locate MAME ROMs that will play with\nWahcade configuration.\nIt's automatically stopped when you are playing a game" \
    --column="" --column="" --column="" \
    --hide-column=2 \
    --separator=" " \
    TRUE  1 "1" \
    FALSE 5 "5" \
    FALSE 10 "10" \
    FALSE 15 "15" \
    FALSE 30 "30" \
    FALSE 60 "60" \
    FALSE 7 "Remove")

if [ "$START" = "" ] ; then
        exit
fi

if [ "$START" = "7" ] ; then
	sed -i '/screensaver/d' /tmp/cron
	crontab /tmp/cron	
	exit
fi

crontab -l | grep screensaver 
if [ $? = 0 ]; then
	temp=`crontab -l | grep screensaver`
	zenity --info --title="Warning" --text="Screensaver already configured \n\n $temp \n\n Please remove first"
	exit
fi

echo "*/$START * * * * DISPLAY=:0 /games/mamelive/scripts/screensaver.sh" >> /tmp/cron
crontab /tmp/cron
