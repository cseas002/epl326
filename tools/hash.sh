#!/bin/bash

for num in 00 01 02 03 04 05 06 07 08 09 {10..99}
do
echo 1026063${num} | openssl dgst -sha256 >> results.txt
done
