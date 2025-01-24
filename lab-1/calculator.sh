#!/bin/bash
echo "Simple Calculator Program"

read -p "Enter value for num1: " num1

read -p "Enter value for num2: " num2


echo "1]Addition"
echo "2]Subtraction"
echo "3]Multiplication"
echo "4]Division"
echo "5]Modulas"
read -p "Enter chioce which operation do you want to perform ? : " chioce
# Check if num1 is even or odd
if [ "$chioce" -eq 1 ]; then
    echo "Addition of $num1 and $num2 is $((num1+num2))"
elif [ "$chioce" -eq 2 ]; then
    echo "Subtraction of $num1 and $num2 is $((num1-num2))"
elif [ "$chioce" -eq 3 ]; then
    echo "Multiplication of $num1 and $num2 is $((num1*num2))"   
 elif [ "$chioce" -eq 4 ]; then
    echo "Division of $num1 and $num2 is $((num1/num2))"  
elif [ "$chioce" -eq 5 ]; then
    echo "Modulas of $num1 and $num2 is $((num1%num2))"     
else
    echo "Invalid Chioce"
fi
