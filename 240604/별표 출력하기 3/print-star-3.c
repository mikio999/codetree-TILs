#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    scanf("%d", &n);
    for (int i = n; i > 0; i--) {
        for (int k = 0; k <= (2*n) - (2*i) - 1; k++) {
            printf(" ");
        }
        for (int j = (2*i) - 1; j > 0; j--) {
            printf("* ");
        }

        printf("\n");
    }
    return 0;
}