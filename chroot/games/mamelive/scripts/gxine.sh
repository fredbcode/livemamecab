#!/bin/sh

set -evx
PATH=/bin:/usr/bin:/sbin:/usr/sbin:/usr/games/:/usr/X11R6/bin/:/usr/bin/X11/


if test -e /dev/sda1
	then
	if test ! -d /tmp/sda1/liveconf/gxine
	 	then
			mkdir /tmp/sda1/liveconf/gxine/ &
			cp -Rf /home/ubuntu/.gxine/* /tmp/sda1/liveconf/gxine/
		fi

	Xdialog --infobox 'USB Drive' 0 0 2000 &
	rm -Rf /home/ubuntu/.gxine
	ln -s /tmp/sda1/liveconf/gxine /home/ubuntu/.gxine &
	gxine &
else
		Xdialog --infobox 'USB Drive not found' 0 0 2000 &
		gxine &
fi

