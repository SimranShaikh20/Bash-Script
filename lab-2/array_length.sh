#!/bin/bash
echo "Finding length of String Array Program"
read -a arr -p "Enter strings separated by spaces: "
for str in "${arr[@]}"
do
  echo "Length of '$str' is: ${#str}"
done