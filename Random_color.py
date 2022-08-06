import random

c = ['X', 'O', 'B', 'X', 'O', # X -> Blue Agent, 先手词, 9个
     'B', 'X', 'O', 'B', 'X', # O -> Red Agent, 后手词, 8个
     'O', 'B', 'X', 'O', 'B', # B -> Innocent Bystander, 中立词, 7个
     'X', 'O', 'B', 'X', 'O', # A -> Assassin, 杀手词, 1个
     'B', 'X', 'O', 'A', 'X']

random.shuffle(c)

print('\n'.join([''.join(['{:3}'.format(item) for item in c[i:i+5]]) for i in range(0, 25, 5)]))
