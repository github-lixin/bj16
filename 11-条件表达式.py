def main():
    a = 10
    b = 20

    if a < b:
        smaller = a
    else:
        smaller = b

    print(smaller)

    s = a if a < b else b  # 与上面的if-else等价，解读为，如果a < b就将a的值赋给S,负责就将b的值赋给s
    print(s)


if __name__ == '__main__':
    main()
