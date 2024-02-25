a ,b = map(int, input().split())

def find_prime_number(n) :
    is_prime = True
    for i in range(2, n) :
        if n%i == 0 :
            is_prime = False
    return is_prime

def solution(a,b) :
    count = 0
    for i in range(a, b+1):
        if find_prime_number(i):
            if i < 10 :
                pass

            else :
                if (int(str(i)[0]) + int(str(i)[1])) % 2 == 0:

                    count += 1
    return count

print(solution(a,b))