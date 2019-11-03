# 将第一个元素认为是有序的，后面的都是无序的，将后面的都插入到前面的正确位置

def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    # 从右边的无序序列中取出多少个元素执行这样的操做
    for j in range(1,n):
        # i = [1,2,3,4,5,6,7,8....n-1]
        i = j
        # 执行从右边无序数列中取出第一个元素，即i位置的元素，然后插入到前面正确的位置中
        while i>0:
            if alist[i] < alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
                # 只要一经交换，i就的变
                i -= 1
            else:
                break


def main():
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    insert_sort(li)
    print(li)


if __name__ == '__main__':
    main()

# 最优时间复杂度：O(n)　　升序序列已经是升序状态
# 最坏时间复杂度：O(n^2)
# 稳定性:稳定
