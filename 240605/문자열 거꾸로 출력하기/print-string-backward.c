#include <stdio.h>
#include <string.h>

int main() {
    char str[10][100];
    for (int i = 0; i < 10; i++) {
        scanf("%s", str[i]);
    }
    for (int i = 0; i < 10; i++) {
        if (strcmp(str[i], "END") != 0) {
            int len = strlen(str[i]);
            for (int j = len - 1; j >= 0; j--) {
                printf("%c", str[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}