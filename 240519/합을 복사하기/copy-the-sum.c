#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int a = 1; int b = 2; int c = 3;
    int three_sum = a+b+c;
    a = b = c = three_sum;
    printf("%d %d %d", a, b, c);
    return 0;
}