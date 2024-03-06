class Game:
  def __init__(self, id, level):
    self.id =id
    self.level = level

player1 = Game('codetree', 10)
print(f'user {player1.id} lv {player1.level}')

a, b = input().split()
player2 = Game(a,b)

print(f'user {player2.id} lv {player2.level}')