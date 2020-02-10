# 输入1-100之间的数，输出除了７和７的倍数
def main():
    for i in range(1,101):
        if i % 7 == 0:
            continue  # 为了结束这次循环开始新的循环
        else:
            print(i,end=" ")


if __name__ == '__main__':
    main()
