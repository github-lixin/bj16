# 希尔排序－其实就是对插入排序的一个改进版

def shell_sort(alist):
	"""希尔排序"""
	n = len(alist)
	gap = n//2  # 这是第一次取的，如果n＝９时　python3会取到小数，因此就需要用 // 来取
	# gap变化到０之前插入算法执行的次数
	while gap >= 1:
		# 插入算法与普通算法的区别就是gap步长
		for j in range(gap,n):
			i = j 
			# 单个元素再执行插入时该放的位置
			while i > 0:
				if alist[i] < alist[i-gap]:
					alist[i],alist[i-gap] = alist[i-gap],alist[i]
				else:
					break 

		# 缩短gap步长
		gap //= 2  # 这是循环不停的取，直到步长小于１


def main():
	li = [54,26,93,17,77,31,44,55,20]
	print(li)
	shell_sort(li)
	print(li)



if __name__ == '__main__':
	main()


# 最优时间复杂度：根据步长序列的不同而不同
# 最坏时间复杂度:Ｏ(n^2)
# 稳定性:不稳定








