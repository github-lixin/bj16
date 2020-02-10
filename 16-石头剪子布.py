import random

all_choices = ['石头','剪子','布']
computer = random.choice(all_choices)  # random模块中有一个choice函数，是在指定的序列中选择一个随机元素返回
player = input('请出拳: ')
print("you choice: %s \ncomputer choice: %s" %(player,computer))
if player == '石头':
    if computer == '石头':
        print('平局')
    elif computer == '剪子':
        print('You WIN')
    else:
        print('You lose')
elif player == '剪子':
    if computer == '剪子':
        print('平局')
    elif computer == '布':
        print('You WIN')
    else:
        print('You lose')
else:
    if computer == '布':
        print('平局')
    elif computer == '石头':
        print('You WIN')
    else:
        print('You lose')
