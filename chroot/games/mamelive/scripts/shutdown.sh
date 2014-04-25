#!/bin/sh

set -evx
PATH=/bin:/usr/bin:/sbin:/usr/sbin:/usr/games/:/usr/X11R6/bin/:/usr/bin/X11/

zenity --info --title="Please Wait --- Shutdown" --timeout=2 
sudo /bin/halt


