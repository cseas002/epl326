import subprocess
from sys import argv


def main():
    word = ''
    for i, gadget in enumerate(argv):
        if i == 0:
            continue
        file = open(gadget + ".txt", 'r')
        for line in file.readlines():
            hex_val = subprocess.run(['./printHex', line.strip()], stdout=subprocess.PIPE).stdout.decode('utf-8')
            # print(hex_val)
            word += hex_val
        print(word)


if __name__ == '__main__':
    main()