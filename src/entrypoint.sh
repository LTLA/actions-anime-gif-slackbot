#!/bin/sh -l

/slackbot.py $1 --sentiment "$2" --rating $3 --title "$4"
