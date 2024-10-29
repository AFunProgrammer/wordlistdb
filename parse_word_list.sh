#!/bin/bash

# Arguments: [wordlist]


# Check if a word list file is provided as an argument
if [ $# -eq 0 ]; then
  echo "Please provide a word list file as an argument."
  exit 1
fi

word_list="$1"

# Loop through each line in the word list
while IFS= read -r word; do
  # Extract the first letter of the word
  first_letter="${word:0:1}"

  # Create a filename based on the first letter
  filename="${first_letter}.txt"

  # Append the word to the corresponding file
  echo "$word" >> "$filename"
done < "$word_list"

