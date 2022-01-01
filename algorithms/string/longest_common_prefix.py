'''
    Leetcode - Longest Common Prefix: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
'''


class Solution:
    def longestCommonPrefix(self, strs):
        size = len(strs)

        if size == 0:
            return ''

        result = ''
        strs = sorted(strs)
        sample = strs[0]

        for s in sample:
            if strs[-1].startswith(result + s):
                result += s
            else:
                break

        return result
