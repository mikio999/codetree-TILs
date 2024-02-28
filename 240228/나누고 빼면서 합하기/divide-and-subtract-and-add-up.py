n, m = map(int, input().split())
A = [int(x) for x in input().split()]

def divide_subtract_add(m) :
  result = A[m-1]
  while m != 1 :
    if m%2 == 1:
      m -= 1
      result += A[m-1]

    else :
      m //= 2
      result += A[m-1]

  return result

print(divide_subtract_add(m))