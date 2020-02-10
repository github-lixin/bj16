def gen_fib(l):
    fib = [0,1]
    for i in range(l-len(fib)):
        fib.append(fib[-1] + fib[-2])
    return fib  # 将这个列表返回

# 实例
a = gen_fib(10)
print(a)
print('---' * 20)
n = int(input("length: "))
print(gen_fib(n))  # 这是传入变量n代表的值赋给形参

