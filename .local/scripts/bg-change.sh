#!/bin/bash

while true; do
  find ~/.wallpaper -type f \( -name '*.jpg' -o -name '*.png' -o -name '*.jpeg' -o -name '*.JPG' -o -name '*.PNG' \) -print0 |
    shuf -n1 -z | xargs -0 feh --bg-fill
    sleep 5m
done
