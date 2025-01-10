#!/bin/bash
echo "Welcome to Simple Calculator"

read -p "Enter value for num1: " num1

read -p "Enter value for num2: " num2

read -p "Enter choice which operation do you want to perform (1] Addition 2] Subtraction 3] Multiplication 4] Division): " choice 

if [ "$choice" -eq 1 ]; then
    echo "Addition of $num1 and $num2 is $((num1 + num2))"
elif [ "$choice" -eq 2 ]; then
    echo "Subtraction of $num1 and $num2 is $((num1 - num2))"
elif [ "$choice" -eq 3 ]; then
    echo "Multiplication of $num1 and $num2 is $((num1 * num2))"
elif [ "$choice" -eq 4 ]; then
    if [ "$num2" -ne 0 ]; then
        echo "Division of $num1 and $num2 is $((num1 / num2))"
    else
        echo "Error: Division by zero is not allowed."
    fi
else
    echo "Invalid choice. Please select a valid operation."
fi
