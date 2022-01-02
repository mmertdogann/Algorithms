'''
    Leetcode - Count Primes: https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744
'''


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        counter = 0
        for i in range(3, n):
            flag = True
            j = 2
            while(flag):
                if i % j == 0:
                    flag = False
                elif j == i - 1 and flag == True:
                    counter += 1
                j += 1

        return counter + 1
