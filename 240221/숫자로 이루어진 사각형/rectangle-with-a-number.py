def num_square(n):
    square = [
        [1 for _ in range(n)]
        for _ in range(n)
    ]

    num = 1
    for i in range(n):
        for j in range(n):
            if num < 10:
                square[i][j] = num
                num += 1
            else:
                num = 1
                square[i][j] = num
                num += 1

    for i in range(n):
        for j in range(n):
            print(square[i][j], end = ' ')
        print()

n = int(input())

num_square(n)