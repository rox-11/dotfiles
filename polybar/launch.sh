#!/bin/bash

# terminate already running bar instances
killall -q polybar parrot

polybar parrot

# lanche bar1
echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log
#polybar mybar 1>&1 | tee -a /tmp/polybar1.log & disown
polybar -c ~/.config/polybar/config hh 
polybar -c ~/.config/polybar/bar mybar2
echo "bars lanched"
