#include <stdio.h>

int main() {
    int A[] = {2, 4, 5, 8, 1};

    printf("Address of A is %p\n", A);
    printf("Address of A[0] is %p\n", &A[0]);
    printf("Value of A[0] is %d\n", A[0]);
    printf("Value of A is %d\n\n", *A);

    // Loop it
    printf("Loop through Array to find addresses\n");
    for(int i = 0; i < 5; i++){
        printf("Address of A[%d] is %p\n", i, &A[i]);
        printf("Address of A + %d is %p\n",i, A+i);
        printf("Value of A[%d] is %d\n", i, A[i]);
        printf("Value of A + %d is %d\n\n",i, *(A + i));        
    }

    return 0;
}