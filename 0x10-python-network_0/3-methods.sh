#!/bin/bash
# Prints out all the HTTP request methods allowed by the server
curl -sI "$1" | grep -i 'Allow' | awk '{$1=""; print}' | xargs 
