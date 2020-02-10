# python中，单双引号没有区别，表示一样的含义
sentence1 = 'tom\'s pet is cat'  # 单引号中间还有单引号可以转义，但劲量不这样使用
sentence2 = "tom\'s pet is cat"  # 也可以使用双引号包含单引号
sentence3 = "tom said:\"hello world!\""  # 中间的双引号转义，但劲量不这样使用
sentence4 = 'tom said:"hello world!"'  # 劲量都单双引号使用

# 三个连续的单引号或双引号，可以保存输入格式，允许输入多行字符串
world = """
hello
world
hello
CSDN"""
print(world)

py_str = 'python'
len(py_str)  # 取长度
py_str[0]  # 第一个字符
'python'[0]
py_str[-1]  # 最后一个字符
# py_str[6]  # 错误，索引超出范围
py_str[2:4]  # 切片，起始索引包含，结束索引不包含，也就是索引是2,3的两个字符
py_str[2:]  # 切片，从索引为２的字符取到结尾
py_str[:2]  # 从索引为０取到索引为２之前的字符，也就是0,1
py_str[:]  # 这个切片也就是创建了一个列表的副本，取全部
py_str[::2]  # 步长值为2，默认为1  取出的是pto
py_str[1::2]  #取出yhn,也就是从索引是1开始到结尾，步长为2
py_str[::-1]  # 步长为-1 表示自右向左取
py_str + 'is good'  # 简单的拼接到一块
py_str * 3  # 将字符串重复打印3遍

# 判断字符是否在字符串中
't' in py_str  # 输出为True
'th' in py_str  # 输出为True
'to' in py_str  # 输出为False

