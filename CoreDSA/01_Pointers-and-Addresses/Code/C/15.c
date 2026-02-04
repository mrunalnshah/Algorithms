#include <stdio.h>

void increment(int a){
    a = a + 1;
    printf("Address of a in increment: %p\n", &a);
}

int main(){
    int a;
    a = 10;

    increment(a);

    printf("Address of a in main: %p\n", &a);

    return 0;
}