#include <stdio.h>
#include <string.h>

void reverseString(char* str) {
    int len = strlen(str);
    int i;
    for (i = 0; i < len / 2; i++) {
        char temp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = temp;
    }
}

int main() {
    char str[10][100];
    for (int i = 0; i < 10; i++) {
        scanf("%s", str[i]);
    }
    for (int i = 0; i < 10; i++) {
        if (strcmp(str[i], "END") != 0) {
            reverseString(str[i]);
            printf("%s\n", str[i]);
        }
    }
    return 0;
}