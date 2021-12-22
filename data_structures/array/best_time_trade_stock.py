'''
    Leetcode - Best Time to Buy and Sell Stock II: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        profit = 0
        for i in range(1, size):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
