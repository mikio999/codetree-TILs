#include <stdio.h>
#include <string.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    char str[10];
    int c = 0;
    scanf("%d %d", &a, &b);
    sprintf(str, "%d", a+b);
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == '1') {
            c += 1;
        }
    }
    printf("%d", c);
    return 0;
}