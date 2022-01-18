'''
    Leetcode - First Bad Version: https://leetcode.com/problems/first-bad-version/
'''

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> int:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while(left <= right):
            mid = left + (right-left) // 2
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid - 1

        return left
