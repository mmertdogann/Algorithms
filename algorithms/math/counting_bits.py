'''
    Leetcode - Counting Bits: https://leetcode.com/problems/counting-bits/
'''


class Solution:
    def countBits(self, num: int) -> List[int]:
        counter = [0]
        for i in range(1, num + 1):
            counter.append(counter[i // 2] + i % 2)
        return counter
