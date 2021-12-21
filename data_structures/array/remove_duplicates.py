'''
    Leetcode - Remove Duplicates from Sorted Array: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        k = 0
        for i in range(1, size):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]

        return k + 1
