# Leetcode problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # Save prices for each min price so far
        min_price = prices[0]
        for price in prices:
            # profit would be greater than zero only when greater than min price
            if price > min_price:
                profit = max(profit, price - min_price)
                # update min price so far
            min_price = min(min_price, price)

        return profit
