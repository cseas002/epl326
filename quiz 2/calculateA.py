import re

a = ""
with open("a.txt") as f:
    for line in f:
        hex_string = ''.join(line)
        hex_string = re.sub(r'\w+:', '', hex_string)  # aferese  tis diefthinseis tou stack(aftes p exoun ":")
        hex_string = ''.join(hex_string.split())
        hex_string = hex_string.replace("0x", '')
        hex_bytes = bytes.fromhex(hex_string)

        a += 'A' * len(hex_bytes)
print(a)
print(len(a))
