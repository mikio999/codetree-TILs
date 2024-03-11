N, B = map(int, input().split())
numbers = []

while True:
  if N < B :
    numbers.append(N)
    break
  else :
    if N%B > 0 :
      numbers.append(N%B)
      N = N//B
    elif N%B == 0 :
      numbers.append(0)
      N = N//B

index = len(numbers)
for i in range(index):
  print(numbers[index-i-1], end='')