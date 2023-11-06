def bestTimeToBuyAndSellStock(prices: [int]) -> int:
    # Write your code here.
    profit,minimumPrice=0,prices[0]
    for index in range(1,len(prices)):
        cost=prices[index]-minimumPrice
        profit=max(profit,cost)
        minimumPrice=min(minimumPrice,prices[index])
    return profit
