#!/bin/bash

for pos in 128 192 256
do
for dec in cbc ecb
do
openssl aes-${pos}-${dec} -d -in $1 -k $2 
done
done