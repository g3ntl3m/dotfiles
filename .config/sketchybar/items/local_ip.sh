#!/bin/sh

sketchybar --add item local_ip right \
           --set local_ip        background.color=$ITEM_BG_COLOR \
                                 icon=􁆬  \
                                 icon.font="Hack Nerd Font:Regular:15.0" \
                                 label.color=$WHITE \
                                 script="$PLUGIN_DIR/local_ip.sh"            \
