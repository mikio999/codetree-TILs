n = int(input())
count = 0

for i in range(n):
    a = [int(x) for x in input().split()]
    if (sum(a)/4) >= 60 :
        count += 1
        print('pass')
    else:
        print('fail')
print(count)