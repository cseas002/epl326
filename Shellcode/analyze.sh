#!/bin/bash

# input: executable program. e.g. $bash analyze.sh rop

export ans=`nm -g $1 | grep -A 7 "f1"`  # finds all 8 gadgets

python3 analyze.py $ans