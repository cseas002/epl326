from sys import argv


def find_char(key, characters, character):
    index = characters.index(character)
    index += key
    return characters[index % 26]

K = argv[1]
M = argv[2]

encoded_message = ""
characters = []

for i in range(97, 123):
    characters.append(chr(i))

for i in M:
    encoded_message += find_char(int(K), characters, i)

print(encoded_message)