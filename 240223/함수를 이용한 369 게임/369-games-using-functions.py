a, b = map(int, input().split())

def three_six_nine_game(a,b):
  cnt = 0
  for i in range(a, b+1):
    if i % 3 == 0:
      cnt += 1
    elif '3' in list(str(i)) or '6' in list(str(i)) or '9' in list(str(i)) :
      cnt += 1
  return cnt

print(three_six_nine_game(a,b))