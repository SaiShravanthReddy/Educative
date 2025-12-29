# 122. Best Time to Buy and Sell Stock II
# 10 mins to read, solve 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of profit
        # traverse list
        # keep track of prev and cur, if cur - prev > 0, add to profit
        # return total profit

        profit = 0
        prev = prices[0]

        for index in range(1, len(prices)):
            cur = prices[index]

            if cur - prev > 0:
                profit += cur - prev
            
            prev = cur

        return profit
