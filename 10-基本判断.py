# 判断：单个数据也可作为判断条件，任何一个值为0的数字，空对象都是False，任何非0数字，非空对象都是True
if 3 > 0:
    print('OK')
    print('YES')

if 10 in [10,20,30]:
    print('OK')

if -0.0:
    print('NO')  # 任何值为0的数字都是False

if [1,2]:
    print('OK')  # 非空对象都是True

if ' ':
    print('YES')  # 空格字符也是字符，True

if '':
    print('True')  # 只有引号，中间连空格都没有就是空字符串，输出False
else:
    print('False')
