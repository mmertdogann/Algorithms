'''
    Leetcode - Valid Palindrome: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
'''

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        size = len(filtered)

        for i in range(size):
            j = size - i - 1
            if filtered[i] != filtered[j]:
                return False

        return True
