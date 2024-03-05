n, k, T = input().split()
n = int(n)
k = int(k)

word_list = []

for i in range(n):
  word = input()
  if T in word:
    word_list.append(word)

word_list.sort()
print(word_list[k-1])