import decryption_methods


def main():
    characters = [' ']  # initializing a list with ' '
    msg = open("./puzzles/puzzle1", 'r').read()  # save all the characters of a file in a string

    for i in range(97, 123):
        characters.append(chr(i))  # adding to the list with characters from 'a' to 'z'

    answers = decryption_methods.one_key_substitution(msg, characters)

    for key, answer in enumerate(answers):
        print("key =", key)  # print the key
        print(answer)  # print the decoded message

    print('for key = 5, answer =', answers[5])


if __name__ == "__main__":
    main()
