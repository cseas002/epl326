import decryption_methods


def main():
    msg = open("./puzzles/puzzle4", 'r').read()  # save all the characters of a file in a string

    characters = [' ', '-', ',', '.', '0']  # initializing a list with ' '

    for i in range(97, 123):
        characters.append(chr(i))  # adding to the list with characters from 'a' to 'z'

    answers = decryption_methods.one_key_substitution(msg, characters)

    for key, answer in enumerate(answers):
        print("key =", key)  # print the key
        print(answer)  # print the decoded message

    print('for key = 9, it seems that the "0" is repeated after 39 letters, so let\'s try transposition in that '
          'message:\n')

    print(decryption_methods.transposition(answers[9], 39, 10))


if __name__ == "__main__":
    main()
