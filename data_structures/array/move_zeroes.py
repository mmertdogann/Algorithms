'''
    Leetcode - Move Zeroes: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        size = len(nums)
        z = 0
        for i in range(size):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[z]
                nums[z] = temp

                z += 1
