#include <stdio.h>

void BubbleSort(int* A, int n){
    int temp;
    
    for(int i = 0; i < n; i++){
        for (int j = 0; j < n - 1; j++){
            if(A[j] > A[j + 1]){  
                temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
            }
        } 
    }
}

int main(){
    int A[] = {3, 2, 1, 5, 6, 4};
    BubbleSort(A, 6);

    for(int i = 0; i < 6; i++){
        printf("%d\n", A[i]);
    }

    return 0;
}