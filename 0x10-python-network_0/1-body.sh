#!/bin/bash
# takes URL,sends GET request to URL,displays body of response
curl -sfL "$1" -X GET
