'''
    Leetcode - Best Time to Buy and Sell Stock: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        max_profit = 0
        lowest = 0
        for i in range(size - 1):
            if prices[i + 1] > prices[lowest]:
                diff = prices[i + 1] - prices[lowest]
                if max_profit < diff:
                    max_profit = diff
            else:
                lowest = i + 1

        return max_profit
