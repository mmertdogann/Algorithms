'''
    Leetcode - Power of Three: https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/
'''


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while(n % 3 == 0):
            n = n / 3

        if n == 1:
            return True

        return False
