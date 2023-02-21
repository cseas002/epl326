from sys import argv


def main():
    K = int(argv[1])
    M = argv[2]

    rows = len(M) // K
    if len(M) % K != 0:
        rows += 1

    matrix = [['0'] * K for _ in range(rows)]
    for index, char in enumerate(M):
        row = int(index / K)
        col = index % K
        matrix[row][col] = char

    result = ""
    for i in range(K):
        for j in range(rows):
            result += matrix[j][i]
    print(result)


if __name__ == "__main__":
    main()
