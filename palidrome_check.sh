#!/bin/bash
echo "Palindrome Checking Program"
 
read -p "Enter a string : " str

str=$(echo "$str" | xargs)

if [ "$(echo $str | rev)" == "$str" ]; then
   echo "$str is a Palindrome String"
else
   echo "$str is not a Palindrome String"
fi
