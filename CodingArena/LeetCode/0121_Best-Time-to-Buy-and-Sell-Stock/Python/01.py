"""
Author: Mrunal Nirajkumar Shah
Date  : 4th March, 2026

LeetCode: 121. Best Time to Buy and Sell Stock

[STACK APPROACH]
Solution Description:
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_stock = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < min_stock:
                min_stock = price
            else:
                profit = price - min_stock

                max_profit = max(profit, max_profit)

        return max_profit

def main():
    list_prices = [[7,1,5,3,6,4],
                   [7,6,4,3,1],
                   [1,2,3,4,5,0],
                   [99, 98, 97, 5, 1, 4]]
    
    solve = Solution()

    result = []
    for prices in list_prices:
        result.append(solve.maxProfit(prices))
    
    print(result)

if __name__ == "__main__":
    main()