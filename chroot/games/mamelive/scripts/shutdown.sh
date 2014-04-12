#!/bin/sh

set -evx
PATH=/bin:/usr/bin:/sbin:/usr/sbin:/usr/games/:/usr/X11R6/bin/:/usr/bin/X11/

Xdialog --infobox 'Please Wait --- Shutdown' 0 0 2000 &
sudo halt


