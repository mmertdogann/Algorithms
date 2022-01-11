'''
    Leetcode - Climbing Stairs: https://leetcode.com/problems/climbing-stairs/
'''


class Solution:
    def __init__(self):
        self.dict = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n not in self.dict:
            self.dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dict[n]
