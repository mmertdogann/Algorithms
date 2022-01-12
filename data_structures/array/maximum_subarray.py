'''
    Leetcode - Maximum Subarray: https://leetcode.com/problems/maximum-subarray/
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(1, size):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]

        return max(nums)
