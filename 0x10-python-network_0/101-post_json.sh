#!/bin/bash
# Sends the contents of a JSON file in a POST request to a server.
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
