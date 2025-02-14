#!/bin/bash

# Prompt for the username
read -p "Enter the username to check: " username

# Check if the user exists in the /etc/passwd file
if id "$username" &>/dev/null; then
    echo "User  '$username' exists in the system."
else
    echo "User  '$username' does not exist in the system."
fi
