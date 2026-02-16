#include <stdio.h>

int main() {
    int a;
    int* p;

    a = 10;
    p = &a;

    printf("Address of p is %p\n", p);
    printf("Value at Address stored at p is %d\n\n", *p);

    int b = 20;
    *p = b;

    printf("Address of p is %p\n", p);
    printf("Value at Address stored at p is %d\n\n", *p);

    p = &b;

    printf("Address of p is %p\n", p);
    printf("Value at Address stored at p is %d\n", *p);

    return 0;
}