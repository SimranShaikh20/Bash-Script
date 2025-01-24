
#!/bin/bash
echo "Finding Directory / File in System"

read -p "Enter file or Directory you want to find ? : " f
if [ -f "$f" ]; then
   echo "$f is file "
elif [ -d "$f" ]; then
   echo "$f is Directory"
else 
   echo "$f doesn't Exist in System"
fi


