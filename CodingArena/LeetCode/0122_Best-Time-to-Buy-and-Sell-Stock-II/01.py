"""
Problem: 122. Best Time to Buy and Sell Stock II
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Author: Mrunal Nirajkumar Shah
Date: 26 May, 2026

Time Complexity: O(n)
Space Complexity: O(2)
where n is the size of prices, and 2 is for storing
max_profit and min_stock_price values.
"""

from typing import List

class Solution:
    """
    Input = [7, 1, 5, 3, 6, 4]
    Output = 7
    [1] 5 - 1 = 4
    [2] 6 - 3 = 3
    4 + 3 = 7 (MAX PROFIT)
    """
    def maxProfit(self, prices: List[int]) -> int:
        """
        Keep track of min_stock_price and when you have a bigger stock_price,
        calculate profit and add it to max_profit and buy that bigger stock. 
        if lower price stock arrives, replace the min_stock_price with it.
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0

        max_profit = 0
        min_stock_price = prices[0]

        for price in prices[1:]:
            if price > min_stock_price:
                max_profit += price - min_stock_price
            
            min_stock_price = price

        return max_profit

def main():
    list_prices = [
        [7,1,5,3,6,4],
        [1,2,3,4,5],
        [7,6,4,3,1],
        [],
        [9, 11, 13, 15, 19],
        [10]
    ]

    list_output = [
        7,
        4,
        0,
        0,
        10,
        0
    ]

    solve = Solution()

    results = []
    for prices in list_prices:
        results.append(solve.maxProfit(prices))

    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()