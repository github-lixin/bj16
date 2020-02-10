# 计算1-100之间的偶数之和
# continue 是跳过本次循环剩余的部分，回到循环条件处

sum1 = 0
counter = 0
while counter < 101:
    counter += 1
    if counter % 2:  # 等价于 if counter % 2 == 1
        continue
    sum1 += counter
print('sum1:',sum1)


sum2 = 0
for i in range(1,101):
    if i % 2 == 1:
        continue
    sum2 += i
print('sum2:',sum2)
