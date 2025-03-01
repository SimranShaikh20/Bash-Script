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

# Count the total number of lines in the C program
total_lines=$(wc -l < "$filename")

# Optionally, count only non-empty lines
# non_empty_lines=$(grep -cve '^\s*$' "$filename")

# Display the results
echo "Total number of lines in '$filename': $total_lines"
# echo "Total number of non-empty lines in '$filename': $non_empty_lines"
