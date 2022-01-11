'''
    Leetcode - Single Number: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for key, value in counts.items():
            if value == 1:
                return key
        return 0
