#include <stdio.h>

void Func1(int A[]){}
void Func1(int* A){}

void Func2(int A[][3]){}
void Func2(int (*A)[3]){}

void Func3(int A[][2][2]){}
void Func3(int (*A)[2][2]){}

int main() {
    int A[] = {1, 2};
    Func1(A);

    int B[2][3] = {{2, 4, 6}, {5, 7, 8}};
    // Func1(B); // Won't work as Func1 required int* while we passing (*)[3]
    Func2(B);

    int X[2][4];
    // Func2(X); // Won't Work int (*)[4] required while Func2 is (*)[3]

    int C[3][2][2] = {
        {
            {2, 5}, 
            {7, 9}
        },
        {
            {3, 4},
            {6, 1}
        },
        {
            {0, 8},
            {11, 13}
        }
    };
    Func3(C);

    return 0;
}