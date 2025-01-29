#!/bin/bash

# Get the list of usernames from the /etc/passwd file
usernames=$(cut -d: -f1 /etc/passwd)

# Initialize variables to hold the longest and shortest usernames
longest_username=""
shortest_username=""

# Loop through each username
for username in $usernames; do
    # Check if the longest_username is empty or if the current username is longer
    if [ -z "$longest_username" ] || [ ${#username} -gt ${#longest_username} ]; then
        longest_username=$username
    fi

    # Check if the shortest_username is empty or if the current username is shorter
    if [ -z "$shortest_username" ] || [ ${#username} -lt ${#shortest_username} ]; then
        shortest_username=$username
    fi
done

# Display the results
echo "Longest Username: $longest_username"
echo "Shortest Username: $shortest_username"