'''
    Leetcode - Reverse String: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
'''


class Solution:
    def reverseString(self, s: List[str]) -> None:
        size = len(s)
        half = size // 2

        for i in range(half):
            j = size - 1 - i
            s[i], s[j] = s[j], s[i]
