
#!/bin/bash

# Set the desired password length
PASSWORD_LENGTH=12

# Generate a random password
# Using /dev/urandom to get random bytes and tr to filter and format the output
PASSWORD=$(< /dev/urandom tr -dc 'A-Za-z0-9_@#$%^&*()' | head -c "$PASSWORD_LENGTH")

# Display the generated password
echo "Generated Password: $PASSWORD"
