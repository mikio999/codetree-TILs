a, b = map(int, input().split())
def calculate_two_int(a,b) :
    if a > b :
        first_num = a + 25
        second_num = b * 2
    else :
        first_num = a * 2
        second_num = b + 25
      
    print('{} {} '.format(first_num, second_num), end = '') 

calculate_two_int(a,b)