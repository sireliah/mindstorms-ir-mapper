#!/bin/bash

MOTOR=$2

ANGLE=0
if [[ ! -z $1 ]]; then
    ANGLE=$1
fi

# echo reset > /sys/class/tacho-motor/$MOTOR/command
echo $ANGLE > /sys/class/tacho-motor/$MOTOR/position_sp 
echo run-to-abs-pos >  /sys/class/tacho-motor/$MOTOR/command
