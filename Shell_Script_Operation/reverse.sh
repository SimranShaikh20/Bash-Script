#!/bin/bash
echo "Reverse Number Program"

read -p "Enter a value you want to reverse ? : " num
echo "Reverse number of $num  is : $(echo $num | rev)"    

