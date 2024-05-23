#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    scanf("%d %d",&a,&b);
    a = a + 8;
    b = 3 * b;
    printf("%d\n%d\n%d", a, b, a*b);
    return 0;
}