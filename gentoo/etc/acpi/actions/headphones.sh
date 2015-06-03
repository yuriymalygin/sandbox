#!/bin/sh

case $3 in
  plug) amixer -q set Master unmute ;;
  unplug) amixer -q set Master mute ;;
  *) echo "Usage: $0 {plug|unplug}" ;;
esac
