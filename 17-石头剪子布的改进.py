import random

all_choice = ['石头','剪子','布']
Win_list = [['石头', '剪子'], ['剪子', '布'], ['布', '石头']]
prompt = """
(0) 石头
(1) 剪子
(2) 布
请选择：(0/1/2)"""
computer = random.choice(all_choice)
num = int(input(prompt))
player = all_choice[num]
print("You choice: %s \ncomputer choice: %s" %(player,computer))
if player == computer:
    print('\033[32;1m平局\033[0m')
elif [player, computer] in Win_list:
    print('\033[31;1mYou Win\033[0m')
else:
    print('\033[31;1mYou lose\033[0m')

