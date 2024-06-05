#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    char strs[5][10] = {"apple", "banana", "grape", "blueberry", "orange"};
    char tgt;
    int cnt = 0;
    scanf("%c", &tgt);
    for (int i = 0; i < 5; i++){
        if (strs[i][2] == tgt | strs[i][3] == tgt) {
            printf("%s\n", strs[i]);
            cnt += 1;
        }
    }
    printf("%d", cnt);
    return 0;
}