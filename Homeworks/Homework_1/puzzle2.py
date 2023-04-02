import decryption_methods


def main():
    msg = open("./puzzles/puzzle2", 'r').read()  # save all the characters of a file in a string

    for i in range(1, 250):
        if 478 % i == 0:
            print(i)

    characters = [' ', ',', '.']  # initializing the list

    for i in range(97, 123):
        characters.append(chr(i))  # adding to the list with characters from 'a' to 'z'

    answers = decryption_methods.two_key_substitution(msg, characters)

    for key1, arr in enumerate(answers):
        for key2, answer in enumerate(arr):
            print("key1 =", key1)  # print the key
            print("key2 =", key2)
            print(answer)  # print the decoded message

    print("for key1 = 11 and key2 = 19, answer =")
    print(answers[11][19])


if __name__ == "__main__":
    main()
