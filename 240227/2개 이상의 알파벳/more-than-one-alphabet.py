A = input()

def more_than_two(a) :
  b = list(a)
  if len(set(b)) >= 2 :
    print('Yes')
  else:
    print('No')

more_than_two(A)