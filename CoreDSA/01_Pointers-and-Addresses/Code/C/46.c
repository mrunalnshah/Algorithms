#include <stdio.h>

void A(){
    printf("Hello\n");
}

void B(void (*ptr)()){ // function pointer as argument
    ptr(); // callback function that "ptr" points to
    // callback
}

int main(){

    void (*p)() = A;
    B(p);

    //or
    B(A); // same as previous two statements

    // A is a callback function here.

    return 0;
}