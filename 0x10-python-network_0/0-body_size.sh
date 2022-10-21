#!/bin/bash
# A script that prints out the content length of the IP address passed
curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}'
