#!/bin/bash
echo "Directory Backup Progam "
 
read -p  "Enter the directory to backup :" ans
if [ -d "$ans" ]; then
   tar -czf backup.tar.gz "$ans"
   echo "Backup od $ans is created as backup.tar.gz "
else 
   echo "$ans is not valid "
fi       
