x = input()
word_list = ['L','E','B','R','O','S']

def find_index(a) : 
  if a in word_list:
    print(word_list.index(x))
  else:
    print('None')

find_index(x)