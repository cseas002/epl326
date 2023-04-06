#!/bin/bash

for key in {1..1000000}
do
openssl aes-128-cbc -d -in puzzle5 -out output.txt -k "$key" 2> /dev/null
check=$(file output.txt)
if [[ $check == *"ASCII"* || $check == *"UTF-8"* ]]; then
  echo "$key";
  openssl aes-128-cbc -d -in puzzle5 -out $((key))output.txt -k "$key";
fi
done
rm output.txt