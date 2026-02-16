#include <stdio.h>
#include <string.h> // strlen, 

int main() {
    char c[20];

    c[0] = 'J';
    c[1] = 'O';
    c[2] = 'H';
    c[3] = 'N';
    c[4] = '\0'; // Good standard to end string with null character.

    int length = strlen(c);

    printf("Length: %d\n", length); 

    return 0;
}