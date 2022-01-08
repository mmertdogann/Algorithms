'''
    Leetcode - Longest Substring Without Repeating Characters: https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size = 0
        sub_str = ''

        for letter in s:
            if letter in sub_str:
                sub_str = sub_str[sub_str.find(letter)+1:]

            sub_str += letter

            size_sub = len(sub_str)
            if size_sub > max_size:
                max_size = size_sub

        return max_size
