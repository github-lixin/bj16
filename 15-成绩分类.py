# 从高向低判断
# 从高分向下判断就节省了判断上限
score = int (input('分数: '))  # 外面使用int是将输入的字符型分数转化为整形
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('你要好好努力了')

print('---' * 30)

# 从低分向高分判断
score = int(input('分数'))
if score >= 60 and score < 70:
    print('D')
elif score >= 70 and score < 80:
    print('C')
elif score >= 80 and score < 90:
    print('B')
elif score >= 90:
    print('A')
else:
    print('你要好好努力了')

