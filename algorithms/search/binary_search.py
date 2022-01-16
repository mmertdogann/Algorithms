'''
    Leetcode - Binary Search: https://leetcode.com/problems/binary-search/
'''


# Leetcode Problem
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid

        return -1


# Recursive
def binary_search(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search(array, element, start, mid - 1)
    else:
        return binary_search(array, element, mid + 1, end)
