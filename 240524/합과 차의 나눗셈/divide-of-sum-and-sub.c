#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int a,b;
    scanf("%d %d", &a, &b);
    float c = (double)(a+b)/(a-b);
    printf("%.2lf",c);
    return 0;
}