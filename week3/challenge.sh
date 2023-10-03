#!/bin/bash
#using bash shell script with touch to create 25 files

NAME="AISHA KHALIFAN"
NUMBER=25

#finding the maximum number of exixting files above prefix
MAX=0

for file in "${NAME}"*; do
  if [[ "$file" =~ ${NAME}([0-9]+) ]]; then
    test=${BASH_REMATCH[1]}
    if (( test > MAX )); then
      MAX=$test
    fi
  fi
done

#finding the starting and ending files
START=$((MAX + 1))
END=$((START + NUMBER - 1))

#create a loop to iterate over

for (( i=START; i<=END; i++ )); do
  touch "${NAME}${i}"
done

#a message to verify that files were created
echo "We created: ${NAME}${START} to ${NAME}${END}"
