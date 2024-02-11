def solution(a, b):
  remainder_count = [0] * b

  while a > 0:
    quotient = a // b
    remainder = a % b

    remainder_count[remainder] += 1
    a = quotient

  squared_count = [count**2 for count in remainder_count]
  sum_of_squared_count = sum(squared_count)

  return sum_of_squared_count

a, b = map(int, input().split())

print(solution(a, b))