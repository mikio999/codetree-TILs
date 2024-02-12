N = int(input())

a = [int(x) for x in input().split()]


def solution(x):
    count = 0
    for i in x:
        if i == max(x):
            count += 1
    
    if count == 1:
        return max(a)
    else:
        return -1
    
print(solution(a))