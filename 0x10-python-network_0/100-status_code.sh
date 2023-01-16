#!/bin/bash
# Sends a request to a web server and only prints the response code.
curl -s -o /dev/null -w '%{http_code}' "$1"
