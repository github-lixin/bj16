import random

num = random.randint(1,100)
counter = 0
while counter < 5:
    answer = int(input('guess a number: '))
    if answer > num:
        print('猜大了')
    elif answer < num:
        print('猜小了')
    else:
        print('猜对了')
        break
    counter += 1
else:  # 循环被break就不会执行，没有被break才会被执行
    print("the number is:",num)
