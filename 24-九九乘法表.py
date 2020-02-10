# 九九乘法表的输出
for i in range(1,10):
    for j in range(1,i+1):
        print('%3s * %s = %3s' %(j,i,i*j),end='')  # end=''是为了不让换行，因为python的print自带换行
    print()  # 此处是为了换行
print('---' * 50)

# 一行代码实现九九乘法表
[print("%3s * %2s = %3s" %(i,j,i*j)) if i == j else print("%s * %s = %s" %(i,j,i*j),end=" ") for i in range(1,10) for j in range(1,i+1)]  
print('---' * 50)


# 对九九乘法表的改进，用户可以指定相乘到多少

n = int(input('number: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('%3s * %2s = %3s' %(j,i,i*j),end=' ')
    print()
