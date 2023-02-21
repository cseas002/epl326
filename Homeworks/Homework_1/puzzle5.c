#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *fp;
    char *words;
    size_t len = 0;
    long k;
    char key[20];
    char command[200];
    char result[200];
    char *msg;

    fp = fopen("/usr/share/dict/words", "r");
    if (fp == NULL) {
        perror("Failed to open words file");
        exit(EXIT_FAILURE);
    }

    fseek(fp, 0, SEEK_END);
    len = ftell(fp);
    fseek(fp, 0, SEEK_SET);
    words = (char*) malloc(len);
    if (words == NULL) {
        perror("Failed to allocate memory for words buffer");
        exit(EXIT_FAILURE);
    }
    fread(words, 1, len, fp);
    fclose(fp);

    for (k = 1000000; k < 1100000; k++) {
        sprintf(key, "%ld", k);
        sprintf(command, "openssl aes-128-cbc -d -in ./puzzles/puzzle5 -out output.txt -k %s 2>&1", key);
        FILE *fp = popen(command, "r");
        if (fp == NULL) {
            perror("Failed to execute command");
            exit(EXIT_FAILURE);
        }
        fgets(result, sizeof(result), fp);
        pclose(fp);

        if (!strstr(result, "bad decrypt")) {
            fp = fopen("output.txt", "r");
            if (fp != NULL) {
                msg = (char*) malloc(len);
                if (msg == NULL) {
                    perror("Failed to allocate memory for message buffer");
                    exit(EXIT_FAILURE);
                }
                fgets(msg, len, fp);
                fclose(fp);
                char *word1 = strtok(msg, " \t\n\r");
                char *word2 = strtok(NULL, " \t\n\r");
                if (word1 != NULL && word2 != NULL && strstr(words, word1) != NULL && strstr(words, word2) != NULL) {
                    printf("%s\n%s %s\n", key, word1, word2);
                    free(msg);
                    break;
                }
                free(msg);
            }
        }
    }

    free(words);
    return 0;
}