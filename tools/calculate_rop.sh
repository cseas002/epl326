#!/bin/bash

# Check if the first argument is provided
if [[ -z "$1" ]]; then
  echo "Usage: $0 <hex_address>"
  exit 1
fi

# Convert the hex address to decimal using printf
dec_address=$(printf "%d" "$1")

# Add 3 to the decimal address
dec_address=$((dec_address + 3))

# Convert the decimal address back to hex using printf
hex_address=$(printf "0x%x" "$dec_address")

# Print the result
echo "$hex_address"
