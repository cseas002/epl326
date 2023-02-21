import decryption_methods


def main():
    msg = open("./puzzles/puzzle3", 'r').read()  # save all the characters of a file in a string
    length = len(msg) - 1  # except the new line character

    characters = [',', '-', ' ', '.']  # initializing the list
    for i in range(65, 91):
        characters.append(chr(i))  # adding to the list with characters from 'A' to 'Z'
    for i in range(97, 123):
        characters.append(chr(i))  # adding to the list with characters from 'a' to 'z
    for i in range(10):
        characters.append(str(i))
    answers = decryption_methods.three_key_substitution(msg, characters)

    # print(answers[8][10][12])
    # for key1, arr in enumerate(answers):
    #     for key2, arr2 in enumerate(arr):
    #         for key3, answer in enumerate(arr2):
    #             for char in answer:
    #                 if char == '\n':
    #                     break
    #                 print("key1 =", key1)
    #                 print("key2 =", key2)
    #                 print("key3 =", key3)
    #                 print(answer)


if __name__ == "__main__":
    main()
