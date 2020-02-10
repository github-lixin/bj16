# break是结束循环，break之后,循环体内代码不再执行

while True:
    yn = input('continue(y/n): ')
    if yn in ['n','N']:
        break
    print('running')
