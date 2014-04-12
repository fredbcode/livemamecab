#!/bin/sh

set -evx
PATH=/bin:/usr/bin:/sbin:/usr/sbin:/usr/games/:/usr/X11R6/bin/:/usr/bin/X11/


if test -e /dev/sda1
	then
	if test ! -r /tmp/sda1/liveconf/beep/config
	 	then
			mkdir /tmp/sda1/liveconf/beep/ &
			cp -Rf /home/ubuntu/.bmp/* /tmp/sda1/liveconf/beep/
		fi

	if test ! -r /tmp/sda1/liveconf/beep/playlist/Play.m3u
		then
			mkdir /tmp/sda1/liveconf/beep/playlist/
			> /tmp/sda1/liveconf/beep/playlist/Play.m3u
		fi
	Xdialog --infobox 'USB Drive' 0 0 2000 &
	rm -Rf /home/ubuntu/.bmp &
	ln -s /tmp/sda1/liveconf/beep /home/ubuntu/.bmp &
	ln -s /tmp/sda1/liveconf/beep/playlist/Play.m3u /home/ubuntu/Playlist.m3u & 
	beep-media-player /tmp/sda1/liveconf/beep/playlist/Play.m3u 
else
		Xdialog --infobox 'USB Drive not found' 0 0 2000 &
		beep-media-player &
fi

