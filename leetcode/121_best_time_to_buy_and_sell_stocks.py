class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimumPrice,profit=prices[0],0
        for index in range(1,len(prices)):
            currentProfit=prices[index]-minimumPrice
            profit=max(profit,currentProfit)
            minimumPrice=min(minimumPrice,prices[index])
        return profit
        