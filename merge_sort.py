def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        return 
    mid = n//2

    # left 采用归并排序后形成的有序的新列表
    left_li = merge_sort(alist[:mid])
    # right 采用归并排序后形成的有序的新列表
    right_li = merge_sort(alist[mid:])

    # 将两个有序的子序列合并成一个整体
    left_pointer, right_pointer = 0, 0

    # 创建一个新列表用于存储排好的列表
    result = []
    # 将两个排序好的子序列排成一个有序的列表
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    # 将存储最准排序好的列表返回---将两边子列表中比较完剩下的数据追加到里面
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result

def main():
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    sorted_li = merge_sort(li)
    print(li)
    print(sorted_li)


if __name__ == '__main__':
    main()
