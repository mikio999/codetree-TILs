#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    scanf("%d", &n);
    if (n >= 100) {
        printf("vapor");
    }
    else if (n >= 0) {
        printf("water");
    }
    else {
        printf("ice");
    }
    return 0;
}