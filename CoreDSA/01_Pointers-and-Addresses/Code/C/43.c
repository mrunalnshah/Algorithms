#include <stdio.h>

int* Add(int* a, int* b) { // called function 
    int* c = (int*) malloc(sizeof(int));

    *c = (*a) + (*b); // a and b pointers to integers local to Add

    return c; // returning the pointer to integer
}

int main() { // calling function
    int a = 2, b = 4;

    // Call by reference
    int* c = Add(&a, &b); // a and b are integers local to main

    printf("%d\n", *c);

    return 0;
}