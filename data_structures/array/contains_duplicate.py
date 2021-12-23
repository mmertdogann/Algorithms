'''
    Leetcode -  Contains Duplicate: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for key in counts:
            if counts[key] > 1:
                return True

        return False
