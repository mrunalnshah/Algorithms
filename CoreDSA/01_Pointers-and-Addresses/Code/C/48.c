#include <stdio.h>
#include <stdlib.h>

int compare(int a, int b){
    if (a > b) {
        return -1; // descending; 1 for ascending.
    } else {
        return 1; // descending; -1 for ascending.
    }
}

int absolute_compare(int a, int b){
    if (abs(a) > abs(b)){
        return 1;
    } else {
        return -1;
    }
}

void BubbleSort(int* A, int n, int (*compare)(int, int)){
    int temp;
    
    for(int i = 0; i < n; i++){
        for (int j = 0; j < n - 1; j++){
            if(compare(A[j], A[j + 1]) > 0){  
                temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
            }
        } 
    }
}

int main(){
    printf("compare\n");
    int A[] = {3, 2, 1, 5, 6, 4};
    BubbleSort(A, 6, compare);

    for(int i = 0; i < 6; i++){
        printf("%d\n", A[i]);
    }

    printf("absolute_compare\n");
    int B[] = {-31, 22, -1, 50, -6, 4};
    BubbleSort(B, 6, absolute_compare);

    for(int i = 0; i < 6; i++){
        printf("%d\n", B[i]);
    }


    return 0;
}