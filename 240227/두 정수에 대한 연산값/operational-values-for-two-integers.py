a, b = map(int, input().split())
def calculate_two_int(a,b) :
    if a > b :
        b *= 2
        a += 25
    else :
        b += 25
        a *= 2
    return a, b

a, b =calculate_two_int(a,b)
print(a,b)