#!/bin/bash
# Sends a GET request to a URL, adds a new request header and outputs the body of the response
curl -s -X GET -H "X-School-User-Id: 98" "$1"
