def find_char(key, characters, character):
    """
    :param key: the key value (amount of characters to shift)
    :param characters: the characters list (list with ' ' and from 'a' to 'z'
    :param character: the character to be shifted with $key characters to the right (clockwise)
    :return: the character in this cipher
    """
    index = characters.index(character)  # find the index of the character
    index -= key  # subtract the key to that index (because in encryption we add)
    return characters[index % len(characters)]  # find the character with the new index


def transposition(msg, rows, cols):
    """
    :param msg: the message to be transpositioned
    :param rows: the number of rows of the matrix
    :param cols: the number of columns of the matrix
    :return: the transpositioned message
    """
    matrix = [['0'] * cols for _ in range(rows)]  # initializing the matrix

    for index, char in enumerate(msg):
        if char == '\n':
            break
        row = index % rows  # goes 0, 1, 2, ...
        col = index // rows  # goes 0, then after (rows amount) 2
        matrix[row][col] = char

    decoded_message = ""

    for arr in matrix:
        for char in arr:
            decoded_message += char

    return decoded_message + '\n'


def one_key_substitution(msg, characters):
    """
    Substitute each character based on a key (shift) in `characters` alphabet
    :param msg: the message to decode
    :param characters: the characters list (alphabet)
    :return: list of all the answers (for each possible key)
    """
    answers = []
    for key in range(len(characters)):  # for every possible key (which is the number of characters to pass
        # (e.g. for key = 1, message = 'a', the decoded message will be 'b'
        decoded_message = ""  # the decoded string
        for char in msg:  # for every character in the file
            if char == '\n':  # ignore the new line character
                decoded_message += '\n'
            else:
                decoded_message += find_char(key, characters, char)
            # find the right character to be substituted and add it to the decoded string
        answers.append(decoded_message)

    return answers


def two_key_substitution(msg, characters):
    """
    Substitute each character based on two keys (shift) in `characters` alphabet
    :param msg: the message to decode
    :param characters: the characters list (alphabet)
    :return: 2D list of all the answers (for each possible key combinations)
    e.g. answers[1][2] = key1 = 1 and key2 = 2
    """
    answers = [['0'] * len(characters) for _ in range(len(characters))]  # initializing the answers matrix
    for key in range(len(characters)):
        for key2 in range(len(characters)):
            decoded_message = ""  # the decoded string
            for i in range(0, len(msg), 2):  # for every character in the file
                if msg[i] == '\n':  # ignore new line character
                    decoded_message += '\n'
                elif msg[i + 1] == '\n':  # ignore new line character
                    decoded_message += find_char(key, characters, msg[i])
                    decoded_message += '\n'
                else:
                    decoded_message += find_char(key, characters, msg[i])
                    decoded_message += find_char(key2, characters, msg[i + 1])
            answers[key][key2] = decoded_message

    return answers


def three_key_substitution(msg, characters):
    """
    Substitute each character based on three keys (shift) in `characters` alphabet
    :param msg: the message to decode
    :param characters: the characters list (alphabet)
    :return: 3D list of all the answers (for each possible key combinations)
    e.g. answers[1][2][3] = key1 = 1, key2 = 2 and key3 = 3
    """
    file = open('answers3.txt', 'w')

    # answers = [[['0'] * len(characters) for _ in range(len(characters))] for _ in range(len(characters))]

    # initializing the answers matrix
    for key in range(len(characters)):
        for key2 in range(len(characters)):
            for key3 in range(len(characters)):
                decoded_message = ""  # the decoded string
                for i in range(0, len(msg), 3):  # for every character in the file
                    if msg[i] == '\n':  # ignore new line character
                        decoded_message += '\n'
                    elif msg[i + 1] == '\n':  # if the second character is the new line character
                        decoded_message += find_char(key, characters, msg[i])  # substitute the first character
                        decoded_message += '\n'
                    elif msg[i + 2] == '\n':  # if the third character is the new line character
                        decoded_message += find_char(key, characters, msg[i])  # substitute the two first characters
                        decoded_message += find_char(key2, characters, msg[i + 1])
                        decoded_message += '\n'
                    else:
                        decoded_message += find_char(key, characters, msg[i])  # substitute the three characters
                        decoded_message += find_char(key2, characters, msg[i + 1])
                        decoded_message += find_char(key3, characters, msg[i + 2])
                # answers[key][key2][key3] = decoded_message
                file.write("key1 = " + str(key) + " key2 = " + str(key2) + " key3 = " + str(key3) + '\n')
                file.write(decoded_message)
                file.close()

    # return answers
