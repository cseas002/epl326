from sys import argv


def find_char(key, characters, character):
    index = characters.index(character)
    index += key
    return characters[index % 28]


def main():
    m = argv[1]

    if m == "snf  r!tt riy0usuonp0d cc t0eoykco0":
        rows = 7  # = len(m) // key (I see 0 after 6 characters)
        key = 5

        matrix = [['0'] * key for _ in range(rows)]
        for index, char in enumerate(m):
            col = index // rows
            row = index % rows
            matrix[row][col] = char

        result = ""
        for i in range(rows):
            for j in range(key):
                result += matrix[i][j]
        print(result)
        return

    characters = [' ']
    for i in range(97, 123):
        characters.append(chr(i))
    characters.append('!')

    for key in range(28):
        decoded_message = ""
        for i in m:
            decoded_message += find_char(key, characters, i)
        if decoded_message == "students should be studying harder":
            print("Plaintext = students should be studying harder")
            print("Cipher and Key = ' ', then a to z and then '!' with key =", key)
            return
        # students should be studying harder

    for key in range(28):
        for key2 in range(28):
            decoded_message = ""
            for i in range(0, len(m), 2):
                decoded_message += find_char(key, characters, m[i])
                decoded_message += find_char(key2, characters, m[i + 1])
            if decoded_message == "students of ucy rule in crypto":
                print("Plaintext = students of ucy rule in crypto")
                print("Cipher and Key = ' ', then a to z and then '!' with keys =", key, "and", key2)
                return
            # students should be studying harder
            # print(decoded_message)


def trans(message, key):
    rows = len(message) // key
    if len(message) % key != 0:
        rows += 1

    matrix = [['0'] * key for _ in range(rows)]
    for index, char in enumerate(message):
        row = int(index / key)
        col = index % key
        matrix[row][col] = char

    result = ""
    for i in range(key):
        for j in range(rows):
            result += matrix[j][i]
    print(result)


if __name__ == "__main__":
    main()
