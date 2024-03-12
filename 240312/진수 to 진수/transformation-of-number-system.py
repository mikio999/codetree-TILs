a, b = map(int, input().split())
n = int(input())

def decimal_generator(y,x):
  x_list = list(str(x))
  num = 0
  for i in range(len(x_list)):
    num = y * num + int(x_list[i])
  return num


def b_generator(d,b):
  digits = []
  while True:
    if d < b:
      digits.append(d)
      break
    digits.append(d%b)
    d = d//b
  return reversed(digits)

def solution(a,b,n) :
  decimal_num = decimal_generator(a,n)
  digit_list = b_generator(decimal_num,b)
  for digit in digit_list :
    print(digit, end='')

solution(a,b,n)