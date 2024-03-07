class Mission:
  def __init__(self, code, color, sec) :
    self.code = code
    self.color = color
    self.sec = sec

code, color, sec = input().split()
mission1 = Mission(code, color, int(sec))

print(f'code : {mission1.code} \ncolor : {mission1.color}\nsecond : {mission1.sec}')