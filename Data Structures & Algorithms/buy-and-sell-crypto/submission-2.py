class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = 100
        profit = 0

        for i in range(len(prices)):
            minimum = min(minimum, prices[i])
            profit = max(profit, prices[i] - minimum)

        return profit