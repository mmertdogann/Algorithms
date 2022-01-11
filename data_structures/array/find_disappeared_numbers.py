'''
    Leetcode - Find All Numbers Disappeared in an Array: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
'''


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        size = len(nums)
        hash_map = {}
        missing = []

        for num in nums:
            hash_map[num] = num

        for num in range(1, size + 1):
            if num not in hash_map:
                missing.append(num)

        return missing
