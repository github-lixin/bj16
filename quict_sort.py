# 递归嵌套
def quick_sort(alist,first,last):
    """快速排序"""
    if first >= last:
        return

    # n = len(alist)
    mid_value = alist[first]
    low = first
    hight = last

    while low < hight:
        # 让hight 左移　　着两个循环可以随便找一个来处理 = 这个特殊情况
        while low < hight and alist[hight] >= mid_value:
            hight -= 1
        alist[low] = alist[hight]
        # low += 1
        # 让　low 右移

        while low < hight and alist[low] < mid_value:
            low += 1
        alist[hight] = alist[low]
        # hight -= 1
            # 从循环退出时：low == high
    alist[low] = mid_value     # 此时就将那个mid_value赋值放到中间，可以是alist[hight] = mid_value  也可以是alist[low] = mid_value,毕竟现在low与hight是相等的
    # 第一次比较完之后
    # alist[:low-1]
    # alist[low+1:]
    # 对　low 左边的列表执行快速排序   用了递归来操作
    quick_sort(alist,first,low-1)
    # 对 low 右边的列表执行快速排序
    quick_sort(alist,low+1,last)



def main():
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    quick_sort(li,0,len(li)-1)
    print(li)


if __name__ == '__main__':
    main()

# 最优时间复杂度：Ｏ(nlogn)
# 最坏时间复杂度：O(n^2)
# 稳定性：不稳定



