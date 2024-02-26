a = input()

def is_palindrome(a):
  b = list(a)
  c = list(reversed(b))
  if c == b:
    print('Yes')
  else:
    print('No')

is_palindrome(a)