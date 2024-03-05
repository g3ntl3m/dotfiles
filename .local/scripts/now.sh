#!/bin/sh

while true; do printf '\033[2J\033[H'; date | figlet -f big -ctW; sleep 1; done
