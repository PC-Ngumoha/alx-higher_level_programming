#!/bin/bash
# Sends the contents of a JSON file in a POST request to a server.
curl -X POST "$1" -H "Content-Type: application/json" -d @"$2"
