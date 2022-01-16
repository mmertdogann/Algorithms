'''
    Leetcode - Find Smallest Letter Greater Than Target: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
'''


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = 0
        size = len(letters)
        while i < size:
            min_str = letters[i]
            if min_str <= target:
                i += 1
            else:
                return min_str

        return letters[0]
