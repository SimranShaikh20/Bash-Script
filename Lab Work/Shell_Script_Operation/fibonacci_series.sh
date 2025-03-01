#!/bin/bash
echo "Fibonacci Series Program"

read -p "Enter a value for n: " num
f0=0
f1=1
echo "Numbers are:"

for ((i=0; i<num; i++)); do
    echo "$f0"
    ans=$((f0 + f1))
    f0=$f1
    f1=$ans
done

