class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = [0] * len(prices)
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
            p1[i] = max_profit

        p2 = [0] * len(prices)
        max_price = prices[len(prices) - 1]
        max_profit = 0
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > max_price:
                max_price = prices[i]
            if max_price - prices[i] > max_profit:
                max_profit = max_price - prices[i]
            p2[i] = max_profit
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, p1[i] + p2[i])
        return max_profit

