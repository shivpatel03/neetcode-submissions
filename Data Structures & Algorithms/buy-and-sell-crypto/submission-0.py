class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #iterate through the array
        #i is the selling value, so record

        # code would be like:
        # go through list
        # if current number - 

        profit = 0
        lowest = prices[0]
        for i in range(len(prices)):
            if (lowest > prices[i]):
                lowest = prices[i]
            profit = max(profit, prices[i] - lowest)

        return profit