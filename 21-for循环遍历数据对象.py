astr = 'hello'  # 字符串
alist = [10,20,30]  # 列表
atuple = ('bob','tom','alice')  # 元组
adict = {'name':'john','age':23}  # 字典

# python 的print有换行的功能
for ch in astr:
    print(ch)
print('---' * 15)

for i in alist:
    print(i)

print('---' * 15)

for name in atuple:
    print(name)

print('---' * 15)

for key in adict:
    print("%s: %s" %(key,adict[key]))
