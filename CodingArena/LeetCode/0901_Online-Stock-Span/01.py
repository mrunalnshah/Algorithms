"""
Problem: 901. Online Stock Span
Link: https://leetcode.com/problems/online-stock-span/description/

Author: Mrunal Nirajkumar Shah
Date: 6 June, 2026

Time Complexity: O(n)
Space Complexity: O(n)

where n is the number of prices in test case.
"""

class StockSpanner:
    """
    Input = [100, 80, 60, 70, 60, 75, 85]
    Output = [1, 1, 1, 2, 1, 4, 6]

    [0]: nothing before 100
    [1]: 100 <= 80
    [5]: 60 <= 75, 70 <= 75, 60 <= 75, but 80 !<= 75 therefore 3 + (1 itself) = 4
    """
    def __init__(self):
        """
        Keep track of all prices before
        """
        self.m_stack = []

    def next(self, price: int) -> int:
        """
        by default, every price has 1 + number of smaller price before. read all values from
        reverse order in stack and continue until bigger value found. keep adding += 1 to consecutive count.
        later append the price to stack and return count.
        """
        consecutive_count = 1
        
        for p in self.m_stack[::-1]:
            if p <= price:
                consecutive_count += 1
            else:
                break

        self.m_stack.append(price)

        return consecutive_count

def main():
    stockSpanner = StockSpanner()
    print(stockSpanner.next(100))
    print(stockSpanner.next(80))
    print(stockSpanner.next(60))
    print(stockSpanner.next(70))
    print(stockSpanner.next(60))
    print(stockSpanner.next(75))
    print(stockSpanner.next(85))

if __name__ == "__main__":
    main()