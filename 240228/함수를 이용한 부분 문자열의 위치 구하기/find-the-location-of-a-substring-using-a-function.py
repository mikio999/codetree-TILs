x = input()
y = input()

def find_location(x,y):
  if y in x :
    for i in range(len(x) - len(y) + 1):
      if x[i:i+len(y)] == y :
        return i
  else :
    return -1
  
print(find_location(x,y))