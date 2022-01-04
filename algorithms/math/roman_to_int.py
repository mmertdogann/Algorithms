'''
    Leetcode - Roman to Integer: https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        size = len(s)
        total = 0
        for i in range(0, size - 1):
            if hash_map[s[i+1]] > hash_map[s[i]]:
                total -= hash_map[s[i]]
            else:
                total += hash_map[s[i]]
        return total + hash_map[s[-1]]
