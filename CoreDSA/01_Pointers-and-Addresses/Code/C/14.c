#include <stdio.h>

void increment(int a){
    a = a + 1;
}

int main(){
    int a;
    a = 10;

    increment(a);

    printf("Value of a = %d\n", a);

    return 0;
}