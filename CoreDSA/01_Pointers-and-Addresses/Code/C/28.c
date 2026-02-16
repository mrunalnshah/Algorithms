#include <stdio.h>

void print(char* C) {
    C[0] = 'A';
    while (*C != '\0'){
        printf("%c", *C);
        C++;
    }

    printf("\n");
}

int main() {
    char c[20] = "Hello";

    print(c); 

    return 0;
}