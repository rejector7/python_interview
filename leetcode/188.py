class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0 or k == 0:
            return 0
        max_profits = [float('-inf')] * k
        min_prices = [float('inf')] * k
        for price in prices:
            min_prices[0] = min(price, min_prices[0])
            max_profits[0] = max(max_profits[0], price - min_prices[0])
            for i in range(1, k):
                min_prices[i] = min(min_prices[i], price - max_profits[i-1])
                max_profits[i] = max(max_profits[i], price - min_prices[i])
        return max_profits[k-1]
