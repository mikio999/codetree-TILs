n =int(input())
even_num = []
a = list(map(int, input().split()))

for i in range(n):
    if a[i]%2 == 0 :
        even_num.append(a[i])

for j in even_num :
    print(j, end=' ')