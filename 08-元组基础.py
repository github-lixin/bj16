# 元组与列表基本上是一样的，只是元组不可便，列表可变
atuple = (10, 20, 30, 'bob', 'alice', [1,2,3])
len(atuple)
10 in atuple
atuple[2]
atuple[3:5]
atuple[-1] = 100 # 错误的，元组是不可变类型
