import random


def random_color():
    c = ['1', '0', '*', '1', '0', # 1 -> Blue Agent, 先手词, 9个
        '*', '1', '0', '*', '1', # 0 -> Red Agent, 后手词, 8个
        '0', '*', '1', '0', '*', # * -> Innocent Bystander, 中立词, 7个
        '1', '0', '*', '1', '0', # X -> Assassin, 杀手词, 1个
        '*', '1', '0', 'X', '1']
    random.shuffle(c)
    print('\n'.join([''.join(['{:3}'.format(item) for item in c[i:i + 5]]) for i in range(0, 25, 5)]))
