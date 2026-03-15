#include <stdio.h>
#include <stdlib.h>

int main(){
	int n;
	  
	printf("Enter size of array\n");
	scanf("%d", &n);  
	
	// int A[n]; // NOT GOOD
	  
	int* A = (int*) malloc(n * sizeof(int));
	  
	for(int i = 0; i < n; i++){
		A[i] = i + 1;
	}

    int* A = (int*) realloc(A, (n/2)*sizeof(int));
	
	for(int i = 0; i < n/2; i++){
		printf("A[%d] = %d\n",i, A[i]);
	}
	
	free(B);
	
	return 0;
}