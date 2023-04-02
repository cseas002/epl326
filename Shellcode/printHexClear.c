#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]){
    char* str = argv[1];
    for (int i = strlen(str) - 1; i >= 0; i--)
        printf("%x", str[i]);

}