# 列表也是序列对象，但他是容器类型，列表中可以包含各种数据
**alist = [10,20,30,'bat','alice',[1,2,3]]
len(alist)
alist[-1]  # 取出最后一项
alist[-1][-1]  # 取出最后一项中的最后一个元素，因为alist的最后一项是列表，因此可以继续取
[1,2,3][-1]  # [1,2,3]是列表[-1]是表示取列表的最后一项
alist[-2][2]  # 取倒数第二个元素，由于alice是字符串，因此可以继续取里面的字符
alist[3:5]  # 切片，取出 bat,alice
10 in alist  # True
'o' in alist  # True
100 not in alist  # True
alist[-1] = 100  # 修改最后一项的值
alist.append(200)  # 向列表中追加一项

