class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            if (prices[i] > max):
                max = prices[i]
                if (max - min > max_profit):
                    max_profit = max - min
            if (prices[i] < min):
                min = prices[i]
                max = prices[i]

        return max_profit
        