n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

k = [a,b,c]
count = 0


for i in k:
    if (sum(i)/4) >= 60 :
        count += 1
        print('pass')
    else:
        print('fail')
print(count)