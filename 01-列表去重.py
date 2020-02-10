 1.使用内置set方法来去重
def main():
    list1 = [2,1,3,4,1]
    list2 = list(set(list1))
    print(list2)


if __name__ == '__main__':
    main()


# 2.使用字典中fromkeys()来去重
def main():
    list1 = [2,1,3,4,1]
    list2 = {}.fromkeys(list1)
    print(list2)

if __name__ == '__main__':
    main()
