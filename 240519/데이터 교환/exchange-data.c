#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int a = 5;
    int b = 6;
    int c = 7;
    int temp;
    int temp2;

    temp = c;
    temp2 = b;
    b = a;
    c = temp2;
    a = temp;

    printf("%d\n%d\n%d\n", a, b, c);
    return 0;
}