a, b = map(int, input().split())
S = [0] * b

while a >= 1:
  c = a//b
  a = c
  d = a%b
  S[d] += 1

sum_square = 0
for i in S:
  k = i * i
  sum_square += k

print(sum_square)