'''
    Leetcode - Missing Number: https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        hash_map = {}

        for num in nums:
            hash_map[num] = num

        for i in range(size + 1):
            if i not in hash_map:
                return i

        return -1
