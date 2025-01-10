
#!/bin/bash
echo "Welcome to Simple Calculator"

read -p "Enter value for num1: " num1

# Check if num1 is even or odd
if [ $((num1 % 2)) -eq 0 ]; then
    echo "It's an even number"
else
    echo "It's an odd number"
fi