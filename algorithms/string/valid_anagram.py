'''
    Leetcode - Valid Anagram: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sizeS = len(s)
        sizeT = len(t)

        if sizeS != sizeT:
            return False

        hash_map = dict()

        for letter in s:
            hash_map[letter] = hash_map.get(letter, 0) + 1

        for letter in t:
            if letter not in hash_map:
                return False
            else:
                hash_map[letter] -= 1

        for letter in hash_map:
            if hash_map[letter] != 0:
                return False

        return True
