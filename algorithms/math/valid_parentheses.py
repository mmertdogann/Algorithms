'''
    Leetcode - Valid Parentheses from Sorted Array: https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/721/
'''


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        hash_map = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in hash_map.values():
                stack.append(c)
            elif c in hash_map.keys():
                if stack == [] or hash_map[c] != stack.pop():
                    return False
            else:
                return False

        return stack == []
