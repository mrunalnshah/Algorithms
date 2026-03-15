#include <stdio.h>
#include <stdlib.h>

int main() {
    int a; // goes on stack

    int* p;
    
    p = (int*)malloc(sizeof(int)); // allocated in heap
    *p = 10;

    p = (int*)malloc(sizeof(int));
    *p = 20;

    free(p);

    p = (int*)malloc(20 * sizeof(int)); //int array of size 20
    p[0] = 5;
    p[1] = 10;
    // etc...

    return 0;
}