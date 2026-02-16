#include <stdio.h>

int SumOfElements(int* A, int size) { // int* A or int A[]
    int sum = 0;

    for(int i = 0; i < size; i++) {
        sum = sum + A[i]; // A[i] or *(A + i)
    }

    return sum;
}

int main() {
    printf("sizeof(int) = %lu\n", sizeof(int));
    printf("sizeof(int*) = %lu\n\n", sizeof(int*));
    
    int A[] = {1, 2, 3, 4, 5};

    int size = sizeof(A) / sizeof(A[0]);
    int total = SumOfElements(A, size); // A or &A[0]

    printf("Sum of Elements = %d\n", total);
    printf("MAIN - Size of A = %lu, size of A[0] = %lu\n", sizeof(A), sizeof(A[0]));

    return 0;
}