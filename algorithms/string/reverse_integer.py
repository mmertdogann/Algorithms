'''
    Leetcode - Reverse Integer: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
'''


class Solution:
    def reverse(self, x: int) -> int:
        limit = 2147483647
        revs_number = 0
        negative_flag = True if x < 0 else False

        if negative_flag:
            x = x * -1

        while (x > 0):
            remainder = x % 10
            revs_number = (revs_number * 10) + remainder
            x = x // 10

        if revs_number > limit:
            return 0

        return (revs_number * - 1) if negative_flag else revs_number
