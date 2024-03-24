n = int(input())
numbers = []

for i in range(n) :
   x = int(input())
   numbers.append(x)

sequence_list = []
k = []
index = 0


for i in range(n):
  if i == n-1:
    if numbers[i] * numbers[i-1] > 0:
      k.append(numbers[i])
      sequence_list.append(k)
    else:
      sequence_list.append(k)
      sequence_list.append(numbers[i])
  elif numbers[i] > 0:
    k.append(numbers[i])
    if numbers[i+1] < 0:
      sequence_list.append(k)
      k = []
  elif numbers[i] < 0:
    k.append(numbers[i])
    if numbers[i+1] > 0:
      sequence_list.append(k)
      k = []
    
length_list = []

for sequence in sequence_list:
  length_list.append(len(sequence))

print(max(length_list))