'''
    Leetcode - Rotate Array: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
'''


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        size = len(nums)
        if k > size:
            k = k % size
        if k > 0:
            nums[:] = nums[size - k:] + nums[0:size - k]
