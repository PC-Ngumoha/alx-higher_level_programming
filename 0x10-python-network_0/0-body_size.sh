#!/bin/bash
# A script that prints out the content length of the IP address passed
curl -sw '%{size_download}' "$1" | tail -n 1 ; echo " "
