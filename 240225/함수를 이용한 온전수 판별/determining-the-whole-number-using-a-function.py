a, b = map(int, input().split())

def find_good_number(a,b) :
    count = 0
    for i in range(a,b+1):
        if i % 2 != 0 :
            if i % 10 != 5 :
                if i % 3 != 0 :
                    count += 1

                else:
                    if i%9 == 0 :
                        count += 1
    return count

print(find_good_number(a,b))