def print_rec(n,m) :
    for i in range(n):
        print('1' * m)
    print()
    
n, m = tuple(map(int, input().split()))
print_rec(n,m)