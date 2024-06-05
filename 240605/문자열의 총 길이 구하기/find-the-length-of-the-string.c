#include <stdio.h>
#include <string.h>

int main() {
    // 여기에 코드를 작성해주세요.
    char arr[10][100];
    int cnt = 0;
    for (int i = 0; i < 10; i++){
        scanf("%s", arr[i]);
    }
    for (int i = 0; i < 10; i++) {
        cnt += strlen(arr[i]);
    }
    printf("%d", cnt);
    return 0;
}