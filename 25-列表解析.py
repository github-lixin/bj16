# 10 + 5的结果放到列表中
[10 + 5]

# 10 + 5 这个表达式计算十次
a = [10 + 5 for i in range(10)]
print(a)

# 10 + i的 i来自与循环
b = [10 + i for i in range(10)]
c = [10 + i for i in range(1,11)]
print(b)
print(c)

# 通过if 过滤，满足条件的才参与10+i的运算
d = [10 + i for i in range(1,11) if i % 2 == 1]
e = [10 + i for i in range(1,11) if i % 2]
print(d)
print(e)

# 生成IP地址列表
f = ['192.168.1.%s' % i for i in range(1,255)]
print(f)
