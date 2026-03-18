#include <stdio.h>
#include <stdlib.h>

// const void* are generic pointers, we can typecast them to pointers of any data type.
int compare(const void* a, const void* b){
    int A = *((int*) a); // typecasting to int* and getting value.
    int B = *((int*) b); 

    return A - B; // B - A for descending
}

int main(){
    int A[] = {-31, 22, -1, 50, -6, 4};
    
    qsort(A, 6, sizeof(int), compare);

    for(int i = 0; i < 6; i++){
        printf("%d\n", A[i]);
    }

    return 0;
}