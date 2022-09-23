import time
import numpy as np
import heapq


# insert sort
def insert_sort(nums):
    """
    >>> insert_sort([5,3,2.1,9,-6])
    [-6, 2.1, 3, 5, 9]
    """
    for j in range(1, len(nums)):
        tmp = nums[j]
        i = j - 1
        while i >= 0 and nums[i] > tmp:
            nums[i + 1] = nums[i]
            i -= 1
        nums[i + 1] = tmp
    return nums


# heap sort
def max_heap(nums,idx,end:int):
    left = (idx<<1)+1
    right = idx+1<<1
    if left <=end and nums[left]>nums[idx]:
        largest = left
    else:
        largest = idx
    if right <= end and nums[right]>nums[largest]:
        largest = right
    if largest!=idx:
        nums[largest],nums[idx] = nums[idx],nums[largest]
        max_heap(nums,largest,end)

def build_max_heap(nums):
    for i in reversed(range(len(nums)//2)):
        max_heap(nums,i,len(nums)-1)

def heap_sort(nums):
    build_max_heap(nums)
    end = len(nums)-1
    for i in range(len(nums)-1,0,-1):
        nums[0],nums[i] = nums[i],nums[0]
        end-=1
        max_heap(nums,0,end)



# 自定义测试
class TestSort:
    def __init__(self, sort=None):
        self.sort = sort
        self.t1 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.t2 = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
        self.t3 = [1, -4, -1, 2, -3, -5, 4, 3, 5, -2, 0]
        self.t4 = [-5, 2, 1, 0, 3, -2, -1, -3, -4, 5, 4]
        self.t5 = [2, -2, 1, -3, 0, -4, -5, 5, 4, 3, -1]

    def test(self):
        self.sort(self.t1)
        self.sort(self.t2)
        self.sort(self.t3)
        self.sort(self.t4)
        self.sort(self.t5)
        print(self.t1, '\n', self.t1, '\n', self.t3, '\n', self.t4, '\n', self.t5)

    def test_time(self):
        nums = np.random.randint(low=-10000, high=10000, size=5000)
        start_time = time.time()
        self.sort(nums)
        end_time = time.time()
        print(f'total_time: {end_time - start_time}')


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    test = TestSort(insert_sort)
    test.test()
    test.test_time()
