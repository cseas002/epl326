import subprocess


def main():
    words = open("/usr/share/dict/words", 'r').read()  # all the words
    for k in range(0, 1000000):
        key = str(k)
        result = subprocess.run(['openssl', 'aes-128-cbc', '-d', '-in', './puzzles/puzzle5', '-out', 'output.txt', '-k',
                                 key], stderr=subprocess.PIPE).stderr.decode('utf-8')

        if not ('bad decrypt' in result):
            try:
                msg = open("output.txt", 'r').read()
                print(k)
                if msg.split()[0] in words and msg.split()[1] in words:
                    print(key)
                    print(msg)
                    break
            except:
                continue

    # os.system('openssl aes-256-cbc -d -in ./puzzles/puzzle5 -out test4.txt -k 1234')
    return


if __name__ == "__main__":
    main()
