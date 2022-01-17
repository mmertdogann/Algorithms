'''
    Leetcode - Two Sum: https://leetcode.com/problems/two-sum/
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        size = len(nums)

        for i in range(size):
            hash_map[nums[i]] = i

        for i in range(size):
            substraction = target - nums[i]
            if substraction in hash_map and hash_map[substraction] != i:
                return [i, hash_map[substraction]]
