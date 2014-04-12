#!/bin/bash

set -vx
cd /tmp
file=`zenity --title="Chose a file:" --file-selection`

case $? in
  0)
    tar -xvf $file | zenity --title="Please wait ..." --progress --pulsate --auto-kill --auto-close 
    cd /tmp/home
    cp -Rf /tmp/home/* /home/
    rm -Rf /tmp/home
    chown -Rf `whoami` $HOME
    zenity --info --text="Done" --timeout=2 ;; 
  1)
    echo "No file";;
  -1)
    echo "No file";;
esac

