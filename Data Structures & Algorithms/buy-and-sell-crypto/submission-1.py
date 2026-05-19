class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum_price = 100
        for i in range(len(prices)):
            minimum_price = min(minimum_price, prices[i])

            profit = max(profit, prices[i] - minimum_price)

        return profit