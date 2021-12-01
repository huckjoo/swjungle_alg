def maxProfit(prices):
    N = len(prices)
    ans = 0
    for i in range(1, N):
        if prices[i-1] < prices[i]:
            ans += prices[i]-prices[i-1]
    return ans


prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))
