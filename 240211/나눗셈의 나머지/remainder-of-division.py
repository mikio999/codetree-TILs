def solution(a, b):
  S = [0] * b

  while a > 0:
    c = a//b
    a = c
    d = a%b
    S[d] += 1

  sum_square = 0
  for i in S:
    k = pow(i, 2)
    sum_square += k

  return sum_square

a, b = map(int, input().split())
print(solution(a, b))