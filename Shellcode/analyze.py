from sys import argv

gadgets = [' ']  # so we can access gadget 1 with g[1], etc.


def hex_to_little_endian(hex_string):
    hex_val = int(hex_string, 16)
    hex_val3 = hex_val + 3
    hex_val3 = hex(hex_val3)[2:]

    if len(hex_val3) % 2 != 0:
        hex_val3 = '0' + hex_val3

    # Convert the hex string to bytes
    hex_bytes = bytes.fromhex(hex_string)
    hex_bytes3 = bytes.fromhex(str(hex_val3))

    # Convert the bytes to little endian order
    little_endian = hex_bytes[::-1]
    little_endian3 = hex_bytes3[::-1]

    # Format the little endian bytes as a string with \x before each byte
    return ''.join([f'\\x{byte:02x}' for byte in little_endian]), ''.join([f'\\x{byte:02x}' for byte in little_endian3])


def main():
    for i in range(1, len(argv), 3):  # goes from one address to the other etc.

        gadget_address = argv[i]
        # subprocess.run(['touch', argv[i + 2] + ".txt"])
        print(argv[i + 2], "address:", gadget_address)
        # Run the system command and capture the output
        gadget_address, gadget_address3 = hex_to_little_endian(gadget_address)

        print("Hex address:", gadget_address)
        print("Hex address + 3:", gadget_address3)
        print()
        # result = subprocess.run(['./printHex', gadget_address], stdout=subprocess.PIPE)
        #
        # # Decode the output from bytes to string
        # output = result.stdout.decode('utf-8')
        #
        # # Print the output
        # print("Hex address:", str(output))

        gadgets.append(gadget_address)


if __name__ == '__main__':
    main()
