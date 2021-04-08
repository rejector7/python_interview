class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum_profit = 0
        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            sum_profit += peak - valley
        return sum_profit
