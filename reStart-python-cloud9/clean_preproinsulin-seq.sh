#!/bin/bash

# Remove ORIGIN, numbers, slashes, spaces, and line breaks.
sed -i 's/\W+//g' preproinsulin-seq.txt

# Confirm that the file has 110 characters.
if [[ $(wc -c preproinsulin-seq.txt) != 110 ]]; then
  echo "The cleaned preproinsulin sequence does not have 110 characters."
  exit 1
fi

cat preproinsulin-seq.txt