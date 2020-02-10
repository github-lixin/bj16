import random

def main():
    num = random.randint(1,10)  # 随机生成一个1-10之间的数包含1 和10,也就是 1<=num<=10
    while True:
        answer = int(input('guess anumber: '))
        if answer > num:
            print('猜大了')
        elif answer < num:
            print('猜小了')
        else:
            print('猜对了')
            print('the number:',num)
            break


if __name__ == '__main__':
    main()
