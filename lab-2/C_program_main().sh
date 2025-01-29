#!/bin/bash

# Check if a filename is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <hello.c>"
    exit 1
fi

# Get the filename from the command line argument
filename="$1"

# Check if the file exists
if [ ! -f "$filename" ]; then
    echo "File '$filename' not found!"
    exit 1
fi

# Search for the 'main' function in the file
if grep -q -E "^\s*int\s+main\s*\(.\)" "$filename" || grep -q -E "^\s*main\s\(.*\)" "$filename"; then
    echo "The file '$filename' contains the 'main' function."
else
    echo "The file '$filename' does not contain the 'main' function."
fi
