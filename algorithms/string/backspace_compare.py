'''
    Leetcode - Backspace String Compare: https://leetcode.com/problems/backspace-string-compare/
'''


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(chars):
            ans = []
            for c in chars:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(s) == build(t)
