def mtable(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print('%3s * %s = %3s' %(i , j, i*j),end='')
        print()

# 实例
mtable(6)
print('--'*30)
mtable(10)

