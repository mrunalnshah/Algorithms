#include <stdio.h>

int Add(int a, int b) { // Called function
    int c = a + b; // a and b are local to Add

    return c;
}

int main() { // calling function
    int a = 2, b = 4;

    // Call by value
    int c = Add(a, b); 
    // value in a of main is copied to a of Add.
    // value in b of main is copied to b of Add.

    printf("%d\n", c);

    return 0;
}