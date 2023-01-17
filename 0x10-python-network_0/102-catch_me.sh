#!/bin/bash
# Trying to make a server return the message "You got me!"
curl -sL -X PUT  -d "You got me!" 0.0.0.0:5000/catch_me
