#!/bin/sh

# Keyboard layout and hotkeys
setxkbmap -layout 'us, ru' -option 'grp:caps_toggle,grp_led:caps,terminate:ctrl_alt_bksp' &

# Load X-resources
xrdb -load .Xdefaults &

# Turning on additional monitor (if connected)
xrandr | grep -qE 'HDMI.* connected' && xrandr --output LVDS1 --off

# Set background image 
feh --bg-tile ~/.background.png

# Run Conky monitoring tool
conky 2>/dev/null &

# Run urxvt daemon for terminals
urxvtd -q -o -f &

# Run ssh-agent for key-forwarding
eval $(ssh-agent -s)

# Auto lock screen if changing position in space
~/.bin/hdaps_screenlock &

# Run WM
exec openbox-session
