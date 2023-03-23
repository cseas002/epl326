/*
 * Control-flow Attack - Defending with Stack Canaries
 * (c) Elias Athanasopoulos,  eliasathan@cs.ucy.ac.cy
 *
 * Compile the attached C program.
 * $ gcc -Wall -no-pie -fno-pic -m32 stack-smash1.c -o stack-smash1
 *
 * Try to reproduce the steps of stack-smash0.c (spot the canary value in the
 * stack).
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int password_valid = 0;

void authenticate_root(char *passwd) {
	unsigned long marker = 0xdeadbeef;
	char password[16];

	strcpy(password, passwd);

	fprintf(stderr, "%p\n", &marker);
	fprintf(stderr, "Validating password: %s\n", password);

	if (!strcmp(password, "e5ce4db216329f4f")) 
		password_valid = marker;

}

int main(int argc, char *argv[]) {

	authenticate_root(argv[1]);

	if (password_valid != 0) {
		printf("Welcome administrator.\n");
	} else {
		printf("Access denied.\n");
	}

	return 1;
}
