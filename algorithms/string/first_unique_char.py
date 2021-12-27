'''
    Leetcode - First Unique Character in a String: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        size = len(s)
        hash_map = dict()

        for i in range(size):
            hash_map[s[i]] = hash_map.get(s[i], 0) + 1

        for i in range(size):
            if hash_map[s[i]] == 1:
                return i
        return -1
