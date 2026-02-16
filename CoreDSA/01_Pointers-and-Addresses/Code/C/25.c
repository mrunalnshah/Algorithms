#include <stdio.h>

// char C[] ~ char* C by compiler (base address)
void print(char C[]) {
    int i = 0;

    // C[i] ~ *(C + i)
    while (C[i] != '\0') { 
        printf("%c", C[i]);
        i++;
    }

    printf("\n");
}

// Pointer variables can be incremented.
void print2(char* C) {
    while (*C != '\0'){
        printf("%c", *C);
        C++;
    }

    printf("\n");
}

int main() {
    char c[20] = "Hello";

    print(c); 
    print2(c);

    return 0;
}