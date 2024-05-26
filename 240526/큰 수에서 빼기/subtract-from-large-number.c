#include <stdio.h>

int main() {
    int a,b;
    // 여기에 코드를 작성해주세요.
    scanf("%d %d",&a, &b);
    if (a > b) {
        printf("%d", a-b);
    }
    if (a < b) {
        printf("%d", b-a);
    }
    else {
        printf("%d", 0);
    }
    return 0;
}