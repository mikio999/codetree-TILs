def LCM(m, n):
    for i in range(max(m, n), (m*n)) :
        if i%m == 0 and i%n == 0:
            return i

m, n = map(int, input().split())

print(LCM(m,n))