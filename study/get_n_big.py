import random


'''
一种不用排序的方法是使用快速选择算法，它可以在平均 O(n) 的时间复杂度内找出第 k 大的元素。

快速选择算法和快速排序算法非常相似，都利用了分治的思想。基本步骤如下：

在数组 arr 中选择一个主元 pivot，可随机选择。
根据主元 pivot 将数组 arr 分成两个部分 left 和 right，其中 left 中的所有元素小于等于 pivot，right 中的所有元素大于 pivot。
如果第 k 大的元素在 left 中，则递归地在 left 中继续查找；否则，递归地在 right 中查找，并更新 k 的值为 k - len(left)。
重复步骤 1 - 3，直到找到第 k 大的元素。
'''

def quick_select(arr, k):
    if not arr:
        return None

    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k <= len(right):
        return quick_select(right, k)
    elif (k - len(right)) <= len(equal):
        return equal[0]
    else:
        return quick_select(left, k - len(right) - len(equal))

if __name__ == '__main__':
    print(quick_select([5,2,3,1],2))