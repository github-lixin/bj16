# 计算1-100相加的和

# 第一种  这个不常用，下面三个常用
sum1 = 0
counter = 1
while counter < 101:
    sum1 += counter
    counter += 1
print(sum1)


# 第二种
sum2 = 0
for i in range(0,100):
    sum2 += (i+1)
print(sum2)


# 第三种
sum3 = sum(range(1,101))
print(sum3)

# 第四种
sum4 = sum([x for x in range(1,101)])
print(sum4)
