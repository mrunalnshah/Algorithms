#include <stdio.h>

int main(){
    int a = 1025;
    int* p;

    p = &a;

    printf("size of integer is %lu\n", sizeof(int));
    printf("address = %p, value = %d\n\n",p, *p);

    // Void Pointer - Generic Pointer
    void* pv;

    pv = p;
    printf("Address = %p, value = %d\n", pv, *pv); // We cannot dereference void pointer.
    printf("Address = %p\n", pv); // We can only print the address.
    
    return 0;
}