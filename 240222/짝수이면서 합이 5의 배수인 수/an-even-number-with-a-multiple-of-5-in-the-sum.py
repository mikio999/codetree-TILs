def say_yes(n) :
    str_n = str(n)
    n_10 = int(str_n[1])
    n_1 = int(str_n[0])
    if (n_10 + n_1) % 5 == 0 and n % 2 == 0:
        return 'Yes'
    else:
        return 'No'

n = int(input())

print(say_yes(n))