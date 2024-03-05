n, k = map(int, input().split())
numbers = [int(x) for x in input().split()]

numbers.sort()
print(numbers[k-1])