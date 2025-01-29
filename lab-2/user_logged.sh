
#!/bin/bash

# Get the username of the current user
current_user=$(whoami)

# Get the login time of the current user
login_time=$(who -u | grep "$current_user" | awk '{print $3, $4}')

# Get the current time
current_time=$(date +"%Y-%m-%d %H:%M:%S")

# Convert login time and current time to seconds since epoch
login_seconds=$(date -d "$login_time" +%s)
current_seconds=$(date -d "$current_time" +%s)

# Calculate the difference in seconds
active_time_seconds=$((current_seconds - login_seconds))

# Convert seconds to hours, minutes, and seconds
active_hours=$((active_time_seconds / 3600))
active_minutes=$(( (active_time_seconds % 3600) / 60 ))
active_seconds=$((active_time_seconds % 60))

# Display the active time
echo "User  '$current_user' has been logged in for: $active_hours hours, $active_minutes minutes, and $active_seconds seconds."



