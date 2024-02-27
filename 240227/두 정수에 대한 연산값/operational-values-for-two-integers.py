a, b = map(int, input().split())
def calculate_two_int(a,b) :
    plus_num = max(a,b) + 25
    multiply_num = min(a,b) * 2
    print('{} {} '.format(multiply_num, plus_num), end = '') 

calculate_two_int(a,b)