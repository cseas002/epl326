from sys import argv


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


def main():
    all_addresses = ""
    if argv[1] == "a":
        for i in range(2, len(argv)):
            gadget_address = hex_to_little_endian(argv[i])
            all_addresses = all_addresses + gadget_address

            print(argv[i] + ":", gadget_address)
            print()
    elif argv[1] == "f":
        # Open the input file
        with open('gadgets.txt', 'r') as file:
            # Read the file line by line and remove the newline character
            addresses = [line.rstrip('\n') for line in file.readlines()]

        for i, address in enumerate(addresses, 1):
            if (len(address.split("#", 1)) > 1):
                gadget = address.split("#", 1)[1].strip()
            else:
                gadget = ""
            address = address.split('#')[0].strip()  # remove the comments #
            if (address):  # if address is not empty
                gadget_address = hex_to_little_endian(address)
                all_addresses = all_addresses + gadget_address
                print(f' {gadget:} {address} => {gadget_address}')
                print()

    print(all_addresses)


if __name__ == '__main__':
    main()
