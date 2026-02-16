#include <stdio.h>

int main() {
    char c[20];

    c[0] = 'J';
    c[1] = 'O';
    c[2] = 'H';
    c[3] = 'N';

    printf("%s", c); // Can show garbage value based on C Compiler

    return 0;
}