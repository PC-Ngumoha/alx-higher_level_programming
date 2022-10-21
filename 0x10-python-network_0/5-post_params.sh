#!/bin/bash
# Sends data to the URL using a POST request method
curl -s -F email="test@gmail.com" -F subject="I will always be here for PLD" "$1"
