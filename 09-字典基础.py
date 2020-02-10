# 字典是key-value(键-值)对形式的，没有顺序，是通过键来取值的
adict = {'name':'bob','age':23}
len(adict)
'bob' in adict  # False
'name' in adict  # True  可以这样查键但值不行
adict['email'] = 'long@119.com'  # 字典中没有键email，那就添加新的键值对
adict['age'] = 25  # 字典中有这个键就是修改这个键锁对应的值

