#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    scanf("%d", &n);
    if (n < 0) {
        printf("ice");
    }
    else if (0 <= n < 100) {
        printf("water");
    }
    else {
        printf("vapor");
    }
    return 0;
}