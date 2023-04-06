#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]){
    char* str = argv[1];
    for (int i = 0; i < strlen(str); i++)
        printf("\\x%x", str[i]);

    printf("\n");
}