'''
    Leetcode - Intersection of Two Arrays II: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
'''


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = dict()
        result = list()
        for i in nums1:
            counts[i] = counts.get(i, 0) + 1

        for item in nums2:
            if item in counts and counts[item] > 0:
                result.append(item)
                counts[item] -= 1
        return result
