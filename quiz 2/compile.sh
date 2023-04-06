#!/bin/bash

# How to assemble:
as --32 shellcode.s -o shellcode.o

# Then, to link:
ld -m elf_i386 shellcode.o -o shellcode

echo "Saving output to shellcode.txt ... "
echo 

objdump -d shellcode | cut -f 2 | grep -A 50 "_start" > shellcode.txt # Prints only the binary collumn

sed -e ':a' -e 'N' -e '$!ba' -e 's/\n */\\x/g' -e 's/  */\\x/g' shellcode.txt > shellcode2.txt

sed 's/\\x\\/\\/g' shellcode2.txt

sed 's/\\x\\/\\/g' shellcode2.txt > shellcode.txt

rm shellcode2.txt