#!/bin/sh

source "$CONFIG_DIR/colors.sh" # Loads all defined colors

if [ $SELECTED = true ]; then
  sketchybar --set $NAME background.drawing=on \
                         background.color=$ITEM_BG_COLOR \
                         label.color=$ACCENT_COLOR \
                         icon.color=$ACCENT_COLOR
else
  sketchybar --set $NAME background.drawing=on \
                         background.color=$ITEM_BG_COLOR \
                         label.color=$WHITE \
                         icon.color=$WHITE
fi
