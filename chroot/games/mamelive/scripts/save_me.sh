#!/bin/bash

set -vx
cd "$HOME"/configurations/Save_me
zenity 	--warning --text="Please wait ... Caution ! There is no backup for artworks and roms - save manually /games" --timeout=3
tar jcfv Backup_$(date +%d-%m-%Y).tar.bz2 $HOME --exclude="$HOME"/configurations/Save_me  2>&1 | zenity --title="Please wait ..." --progress --pulsate --auto-kill --auto-close 
zenity --info --text="Done" --timeout=2
