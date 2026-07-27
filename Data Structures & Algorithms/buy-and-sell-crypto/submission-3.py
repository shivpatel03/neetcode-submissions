class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = 101
        maximum_profit = 0
        left = 0
        right = 0

        for right in prices:
            if right < minimum_price:
                minimum_price = right
            maximum_profit = max(maximum_profit, right - minimum_price)

        return maximum_profit
            