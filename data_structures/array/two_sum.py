'''
    Leetcode - Two Sum: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        hash_map = {}

        for i in range(size):
            hash_map[nums[i]] = i

        for i in range(size):
            complement = target - nums[i]
            if complement in hash_map and hash_map[complement] != i:
                return [i, hash_map[complement]]
