# 121. Best Time to Buy and Sell Stock
# 20 mins to read, solve and debug

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return if len of array is 0,1
        # vars - low, high, profit = 0,0,0
        # initial val l, h = first element
        # traverse the list
        # if val is less than l, replace l and h with val and cal profit
        # if val is higher than h, replace h and cal proit
        # if neither contnue
        # finally return profit

        low, high = prices[0], prices[0]
        profit = 0

        for index in range(1, len(prices)):

            if prices[index] < low:
                low = prices[index]
                high = prices[index]

                if (high - low) > profit:
                    profit = high - low

            elif prices[index] > high:
                high = prices[index]
                
                if (high - low) > profit:
                    profit = high - low
            else:
                continue
        
        return profit

# Educative answer
def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0.0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price, price)
            compare_profit = price - min_price
            max_profit = max(max_profit, compare_profit)

        return int(max_profit)