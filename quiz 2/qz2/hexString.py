from sys import argv

gadgets = [' ']  # so we can access gadget 1 with g[1], etc.


def hex_to_little_endian(hex_string):
    hex_val = int(hex_string, 16)
    hex_val = hex(hex_val)[2:]

    if len(hex_val) % 2 != 0:
        hex_val = '0' + hex_val

    # Convert the hex string to bytes
    hex_bytes = bytes.fromhex(str(hex_val))

    # Convert the bytes to little endian order
    little_endian = hex_bytes[::-1]

    # Format the little endian bytes as a string with \x before each byte
    return ''.join([f'\\x{byte:02x}' for byte in little_endian])


def main():
    for i in range(1, len(argv)):  # goes from one address to the other etc.

        gadget_address = hex_to_little_endian(argv[i])

        print(argv[i] + ":", gadget_address)
        print()


if __name__ == '__main__':
    main()
