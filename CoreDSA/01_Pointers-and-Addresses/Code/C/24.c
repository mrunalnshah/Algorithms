#include <stdio.h>
#include <string.h> // strlen, 

int main() {
    char c[20] = "JOHN"; // Size 20
    char d[] = "JOHN"; // Size 5
    // char e[4] = "JOHN"; // Compilation ERROR
    char f[5] = {'J', 'O', 'H', 'N', '\0'}; // One more way  Size 5


    printf("Size in bytes, c: %lu\n", sizeof(c));
    printf("Size in bytes, d: %lu\n\n", sizeof(d));
    
    int lengthc = strlen(c);
    int lengthd = strlen(d);

    printf("Length, c: %d\n", lengthc); 
    printf("Length, d: %d\n\n", lengthd); 

    return 0;
}