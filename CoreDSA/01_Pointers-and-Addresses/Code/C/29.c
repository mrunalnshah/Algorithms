#include <stdio.h>

// Error: you can't change const variable
void print(const char* C) {
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