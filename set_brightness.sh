#!/bin/bash

# Requirements - ddcutil and sudo privileges
# This script is to be able to use it via terminal using only alias of "display 1" or "display 10" for 10% or 100% brightness settings respectively.
# add alias
# alias display='/root/set_brightness.sh'
# restart terminal or run "source ~/.bashrc"
# enjoy

brightness_level=$1

# Check if brightness level is provided as an argument
if [ -z "$brightness_level" ]; then
  echo "Enter the desired brightness level (0-100):"
  read brightness_level
fi

# Enable single digits *10 values for brightness percent. Use only display 1 or 5 or 10 for respective 10%, 50% ot 100% brightness.
brightness_percentage=$((brightness_level * 10))

# make a new line for every monitor. Check with "ddcutil detect" to see monitors.
# ddcutil setvcp --display=$CHANGE_NUMBER_DISPLAY_HERE 0x10 $brightness_level
ddcutil setvcp --display=1 0x10 $brightness_percentage
ddcutil setvcp --display=2 0x10 $brightness_percentage
