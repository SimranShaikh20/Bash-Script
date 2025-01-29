#!/bin/bash
echo "Greeting based on time Program"

hour=$(date +%H)
if [ $hour -lt 12 ]; then
  echo "Good Morning ..."
elif [ $hour -lt 18 ]; then
   echo "Good Afternoon ..."
else 
    echo "Good Evening ...."
fi        
  
  