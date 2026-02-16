#include <stdio.h>

void print(char* C) {
    while (*C != '\0'){
        printf("%c", *C);
        C++;
    }

    printf("\n");
}

int main() {
    // char c[20] = "Hello"; // string gets stored in the space for array.
    char* c = "Hello"; // String gets stored as compile time constant.

    print(c); 

    return 0;
}