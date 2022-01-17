'''
    Leetcode - Two Sum: https://leetcode.com/problems/two-sum/
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = dict()
        size = len(nums)

        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

        for num in hash_map:
            if hash_map[num] > size // 2:
                return num
